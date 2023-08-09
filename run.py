import os
import tempfile

import openai
import requests
from dotenv import load_dotenv
from pydub import AudioSegment


def download_podcast(podcast_url):
    if not os.path.exists('podcast.mp3'):
        print('Getting podcast')
        response = requests.get(podcast_url)

        with open('podcast.mp3', 'wb') as f:
            f.write(response.content)

def load_audio(file_path):
    print('Loading audio')
    audio = AudioSegment.from_mp3(file_path)
    return audio

def transcribe_audio(audio, model, prompt):
    transcript = ''
    chunk_duration_ms = 5 * 60 * 1000
    audio_length_ms = len(audio)
    num_chunks = int(audio_length_ms / chunk_duration_ms)

    for i in range(num_chunks):
        start_time = i * chunk_duration_ms
        end_time = min((i + 1) * chunk_duration_ms, audio_length_ms)
        chunk = audio[start_time:end_time]

        with tempfile.NamedTemporaryFile(suffix='.mp3', delete=False) as f:
            chunk.export(f.name, format='mp3')
            temp_file_path = f.name
            audio_file = open(temp_file_path, "rb")

        print('Transcribing chunk', i)
        transcript += openai.Audio.transcribe(
            file=audio_file,
            model=model,
            prompt=transcript
        )['text']

        os.remove(temp_file_path)

    return transcript

def save_transcript(transcript, file_path):
    with open(file_path, 'w') as f:
        f.write(transcript)

def main():
    load_dotenv()
    openai.api_key = os.getenv("OPENAI_API_KEY")

    podcast_url = ''
    download_podcast(podcast_url)

    audio = load_audio('podcast.mp3')

    model = "whisper-1"
    prompt = ''
    transcript = transcribe_audio(audio, model, prompt)

    save_transcript(transcript, 'transcript.txt')

if __name__ == "__main__":
    main()
