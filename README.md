# Audio Diarization and Sentiment Analysis
This project provides a web application for audio diarization and sentiment analysis of conversations. Audio diarization is the process of segmenting and labeling an audio recording based on speaker identities, while sentiment analysis aims to extract sentiment or psychological insights from the conversation. This repository contains Python code utilizing Flask, Whisper API, OpenAI API, and Pyannote to achieve these functionalities.

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

It was a very interesting assignment. Unfortunately, I have used all free credits in Google Cloud for my previous projects (from different emails, ouch). But I would definitely deploy it on App engine, amending the existing code by adding google cloud storage client and bucket for user uploads.
The main challenge was that I had several assignments to be done within almost the same timeframe. But I managed my time accordingly.
The problem that I faced is with speechbrain library, it was giving me the error that no library was imported. But it turned out the problem was the new version of speechbrain (i.e. >= 1.0.0) and the pyannote importing from speechbrain.inference for version 1.0 or higher, and fallbacks to speechbrain.pretrained. For that reason I pinned the speechbrain version in requirements.txt. Although while testing I was using version 1 and ammended pyannote library on my local machine.

Upon finishing the project, I reflected on the following points:

* Performance Optimization: Consider optimizing the application for better performance, such as by optimizing code execution, improving concurrency, or implementing caching mechanisms.

* User Experience Enhancements: Enhance the user experience by adding features like real-time progress updates during audio processing, better error handling, or interactive visualizations for analysis results.

* Scalability and Deployment: Think about strategies for scaling the application, such as deploying it to scalable cloud platforms like Google App Engine or Kubernetes for handling increased user traffic.

