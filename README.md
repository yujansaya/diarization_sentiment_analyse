# Audio Diarization and Sentiment Analysis
This project provides a web application for audio diarization and sentiment analysis of conversations. Audio diarization is the process of segmenting and labeling an audio recording based on speaker identities, while sentiment analysis aims to extract sentiment or psychological insights from the conversation. This repository contains Python code utilizing Flask, Whisper API, OpenAI API, and Pyannote to achieve these functionalities.

**Functionality:**
- Users can upload audio files (in WAV, MP3, or M4A formats) through a web interface.<img width="622" alt="Screenshot 2024-04-26 at 1 39 58 PM" src="https://github.com/yujansaya/diarization_sentiment_analyse/assets/109923065/c94e4b2a-bcbb-4f5f-905f-1cca69523a2a">
- Upon upload, the system transcribes the audio using a speaker diarization algorithm.
  <img width="670" alt="Screenshot 2024-04-26 at 1 27 55 PM" src="https://github.com/yujansaya/diarization_sentiment_analyse/assets/109923065/c680f343-b4f8-43ce-a737-d698e1e08250">
<img width="698" alt="Screenshot 2024-04-26 at 1 37 46 PM" src="https://github.com/yujansaya/diarization_sentiment_analyse/assets/109923065/fd67b545-1e91-4f83-8e4e-22f222ca7780">

- It then performs sentiment analysis on the transcribed text.
  <img width="657" alt="Screenshot 2024-04-26 at 1 37 57 PM" src="https://github.com/yujansaya/diarization_sentiment_analyse/assets/109923065/9167b806-545e-43e5-88b6-6a4374184821">
  
- Results, including the transcript and sentiment analysis, are displayed to the user.
  
**Components:**
- main.py: Contains the Flask application, defining routes for file upload and handling, transcribing audio, and performing sentiment analysis using OpenAI.
- diarisation.py: Implements the speaker diarization algorithm using the Pyannote library. It preprocesses the audio, extracts speaker embeddings, performs clustering, and generates a transcript with speaker labels.
- upload.html: HTML template for the upload form and result display. Utilizes JavaScript and jQuery for asynchronous file upload and progress tracking.
  
**Dependencies:**
- Flask: Web framework for Python.
- Pyannote: Library for speaker diarization.
- OpenAI API: Used for sentiment analysis.
- Google Cloud Storage: Used for storing uploaded audio files.
- FFmpeg: Required for audio preprocessing.
- Werkzeug: Utility library for Flask.
- Bootstrap: CSS framework for frontend styling.
  
**Workflow:**
- Users upload an audio file through the web interface.
- The file is processed, transcribed, and analyzed asynchronously.
- Upon completion, the transcript and sentiment analysis results are displayed to the user.
  
**Deployment:**
This Flask application is deployed on Google Cloud, access it through <a href="https://alindor-test.nw.r.appspot.com/">this link</a> 

## Installation
Before running the application, ensure you have Python installed on your system. Additionally, install the required Python packages using pip. The required packages are listed in requirements.txt.
As well there is archived ffmpeg file, please unzip it (if you are using Mac). Other wise you coukd download the file from [this link](https://ffbinaries.com/downloads). 
And please remember to change the path to the ffmpeg file in main.py.
```console
os.environ["PATH"] += os.pathsep + f'YOUR ABSOLUTE PATH TO FFMPEG FILE'
```

## Usage
1. Clone this repository to your local machine:
```console
git clone https://github.com/your_username/your_repository.git
cd your_repository
```

2. Set up your OpenAI API key by replacing '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' in main.py with your own API key.

3. Run the Flask application:

```console
python main.py
```

4. Open your web browser and go to http://127.0.0.1:5000/. You will see a file upload form.

5. Upload an audio file.

6. Wait for the processing to complete. The application will transcribe the audio and perform sentiment analysis. Once done, you will see the transcription and sentiment analysis displayed on the web page.

## File Structure
* main.py: Contains Flask routes for handling file upload, audio diarization, and sentiment analysis.
* diarisation.py: Implements the SpeakerDiarizer class for audio diarization using Pyannote.
* upload.html: HTML template for the file upload form.
  
## Dependencies
* Flask: A micro web framework for Python.
* Pyannote: A toolkit for speaker diarization and speaker embedding.
* Whisper API: Used for transcribing audio.
* OpenAI API: Used for sentiment analysis.
* NumPy: A library for numerical computing.
* scikit-learn: A machine learning library for Python.

## Final thoughts

Upon finishing the project, I reflected on the following points:

* Performance Optimization: Consider optimizing the application for better performance, such as by optimizing code execution, improving concurrency, or implementing caching mechanisms.

* User Experience Enhancements: Enhance the user experience by adding features like real-time progress updates during audio processing, better error handling, or interactive visualizations for analysis results.

* Scalability and Deployment: Think about strategies for scaling the application, such as deploying it to scalable cloud platforms like Google App Engine or Kubernetes for handling increased user traffic.

