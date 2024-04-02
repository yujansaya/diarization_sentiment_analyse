from pyannote.audio import Audio
from pyannote.core import Segment
import contextlib
import wave
import numpy as np
from sklearn.cluster import AgglomerativeClustering
import datetime
import subprocess
import whisper
from google.cloud import storage
import os
from pyannote.audio.pipelines.speaker_verification import PretrainedSpeakerEmbedding
import torch


class SpeakerDiarizer:
    def __init__(self, num_speakers=2):
        self.num_speakers = num_speakers
        self.model = whisper.load_model("small")
        self.embedding_model = PretrainedSpeakerEmbedding("speechbrain/spkrec-ecapa-voxceleb")

    def segment_embedding(self, segment, path, duration):
        start = segment["start"]
        end = min(duration, segment["end"])
        clip = Segment(start, end)
        audio = Audio()
        waveform, sample_rate = audio.crop(path, clip)
        return self.embedding_model(waveform[None])


    def diarize(self, path):
        storage_client = storage.Client()
        bucket_name = 'alindor-uploads'
        bucket = storage_client.bucket(bucket_name)
        blob = bucket.blob(path.replace('gs://' + bucket_name + '/', ''))
        audio_file = '/tmp/audio.wav'
        blob.download_to_filename(audio_file)

        processed_audio_file = '/tmp/audio_processed.wav'
        subprocess.call(['ffmpeg', '-i', audio_file, '-ac', '1', processed_audio_file, '-y'])
        os.remove(audio_file)

        result = self.model.transcribe(processed_audio_file)
        segments = result["segments"]

        with contextlib.closing(wave.open(processed_audio_file, 'r')) as f:
            frames = f.getnframes()
            rate = f.getframerate()
            duration = frames / float(rate)

        embeddings = []
        for segment in segments:
            embeddings.append(self.segment_embedding(segment, processed_audio_file, duration))

        os.remove(processed_audio_file)

        embeddings = np.nan_to_num(np.array(embeddings))
        embeddings = np.concatenate(embeddings, axis=0)
        clustering = AgglomerativeClustering(self.num_speakers).fit(embeddings)
        labels = clustering.labels_

        for i, segment in enumerate(segments):
            segment["speaker"] = 'SPEAKER ' + str(labels[i] + 1)

        def time(secs):
            return datetime.timedelta(seconds=round(secs))

        transcript = ""
        for i, segment in enumerate(segments):
            if i == 0 or segments[i - 1]["speaker"] != segment["speaker"]:
                transcript += "\n" + segment["speaker"] + ' ' + str(time(segment["start"])) + '\n'
            transcript += segment["text"][1:] + ' '

        return transcript
