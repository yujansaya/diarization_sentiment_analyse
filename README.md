Audio Diarization and Sentiment Analysis
This project provides a web application for audio diarization and sentiment analysis of conversations. Audio diarization is the process of segmenting and labeling an audio recording based on speaker identities, while sentiment analysis aims to extract sentiment or psychological insights from the conversation. This repository contains Python code utilizing Flask, Google Speech Recognition API, OpenAI API, and Pyannote to achieve these functionalities.

Installation
Before running the application, ensure you have Python installed on your system. Additionally, install the required Python packages using pip:

bash
Copy code
pip install Flask pyannote.audio google-cloud-speech openai-python numpy scikit-learn
Usage
Clone this repository to your local machine:
bash
Copy code
git clone https://github.com/your_username/your_repository.git
cd your_repository
Set up your OpenAI API key by replacing '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' in main.py with your own API key.

Run the Flask application:

bash
Copy code
python main.py
Open your web browser and go to http://127.0.0.1:5000/. You will see a file upload form.

Upload an audio file (supported formats: wav, mp3, m4a).

Wait for the processing to complete. The application will transcribe the audio and perform sentiment analysis. Once done, you will see the transcription and sentiment analysis displayed on the web page.

File Structure
main.py: Contains Flask routes for handling file upload, audio diarization, and sentiment analysis.
diarisation.py: Implements the SpeakerDiarizer class for audio diarization using Pyannote.
upload.html: HTML template for the file upload form.
Dependencies
Flask: A micro web framework for Python.
Pyannote: A toolkit for speaker diarization and speaker embedding.
Google Cloud Speech-to-Text API: Used for transcribing audio.
OpenAI API: Used for sentiment analysis.
NumPy: A library for numerical computing.
scikit-learn: A machine learning library for Python.
