from flask import Flask, render_template, request, jsonify
from werkzeug.utils import secure_filename
import os
from diarisation import SpeakerDiarizer
from openai import OpenAI
from concurrent.futures import ThreadPoolExecutor

# Set up OpenAI API key
OPENAI_API_KEY = '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'
client = OpenAI(api_key=OPENAI_API_KEY)

os.environ["PATH"] += os.pathsep + f'YOUR ABSOLUTE PATH TO FFMPEG FILE'

app = Flask(__name__)

# Define the directory to store uploaded files
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'wav', 'mp3', 'm4a'}  # Allowed audio file extensions
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
NUMBER_SPEAKERS = 2

#Function to check if the file extension is allowed
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


# Function to transcribe audio using Google Speech Recognition API
def transcribe_audio(audio):
    diarizer = SpeakerDiarizer(num_speakers=NUMBER_SPEAKERS)
    transcript = diarizer.diarize(audio)
    print(transcript)
    return transcript


# Function to perform sentiment analysis using OpenAI API
def analyze_sentiment(text):
    response = client.completions.create(
        model="gpt-3.5-turbo-instruct",
        prompt=f"Analyze the conversation and get sentiment or psychological insights derived from the conversation, as well give separte insights about each speaker. DO NOT INVENT if there is not much information from dialogue. Be precise and concise. Conversation:{text}",
        temperature=0.5,
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
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        print(filepath)
        file.save(filepath)
        # Asynchronous processing with ThreadPoolExecutor
        with ThreadPoolExecutor() as executor:
            # Transcribe audio in a separate thread
            transcript_future = executor.submit(transcribe_audio, filepath)
            # Analyze sentiment in a separate thread
            sentiment_future = executor.submit(analyze_sentiment, transcript_future.result())

            # Wait for both tasks to complete
            transcript = transcript_future.result()
            sentiment_analysis = sentiment_future.result()
            return jsonify({'transcript': transcript, 'sentiment_analysis': sentiment_analysis})
    else:
        return jsonify({'error': 'Invalid file format'})


if __name__ == "__main__":
    app.run(debug=True)
