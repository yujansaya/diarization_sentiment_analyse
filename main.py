from flask import Flask, render_template, request, jsonify
from werkzeug.utils import secure_filename
import os
from diarisation import SpeakerDiarizer
from openai import OpenAI
from google.cloud import storage

# os.system("pip install git+https://github.com/openai/whisper.git")
# Set up OpenAI API key
OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')
client = OpenAI(api_key=OPENAI_API_KEY)

#os.environ["PATH"] += os.pathsep + f'/Users/zhansayayussupova/PycharmProjects/alindor/'

app = Flask(__name__)
# Configure Google Cloud Storage client
storage_client = storage.Client()

# Define the Google Cloud Storage bucket name
BUCKET_NAME = 'alindor-uploads'
bucket = storage_client.bucket(BUCKET_NAME)

#os.environ["PATH"] += os.pathsep + f'gs://staging.alindor-test.appspot.com/ffmpeg'
# Get the directory of the current file
current_directory = os.path.dirname(os.path.abspath(__file__))
# Specify the path to ffmpeg
ffmpeg_path = os.path.join(current_directory, 'ffmpeg')
os.environ["PATH"] += os.pathsep + ffmpeg_path

# Define the directory to store uploaded files
#UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'wav', 'mp3', 'm4a'}  # Allowed audio file extensions
#app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
NUMBER_SPEAKERS = 2
diarizer = SpeakerDiarizer(num_speakers=NUMBER_SPEAKERS)
#ffmpeg_path = os.path.join("gs://staging.alindor-test.appspot.com/ffmpeg")

# Function to check if the file extension is allowed
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


# Function to transcribe audio using Google Speech Recognition API
def transcribe_audio(audio):
    transcript = diarizer.diarize(audio)
    print(transcript)
    return transcript


# Function to perform sentiment analysis using OpenAI API
def analyze_sentiment(text):
    response = client.completions.create(
        model="gpt-3.5-turbo-instruct",
        prompt=f"Please analyze the dialogue transcripts and provide insights about the individuals involved, including their relationships, emotions, and personalities, based solely on the information present in the transcripts. If the transcripts do not contain sufficient data to draw meaningful conclusions, please indicate so rather than generating speculative insights. Transcript:{text}",
        temperature=0.7,
        max_tokens=500
    )
    return response.choices[0].text.strip()


# Route for rendering upload form
@app.route('/')
def upload_form():
    return render_template('upload.html')


# Route to handle file upload
@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    print('hello')
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'})
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        blob = bucket.blob(filename)
        blob.upload_from_file(file)
        filepath = f'gs://{BUCKET_NAME}/{filename}'
        print(filepath)

        # Wait for both tasks to complete
        transcript = transcribe_audio(filepath)
        sentiment_analysis = analyze_sentiment(transcript)
        return jsonify({'transcript': transcript, 'sentiment_analysis': sentiment_analysis})
    else:
        return jsonify({'error': 'Invalid file format'})


# if __name__ == "__main__":
#     app.run(host='127.0.0.1', port=8080, debug=True)
