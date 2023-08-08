import os
import tempfile

import openai
import requests
from dotenv import load_dotenv
from pydub import AudioSegment

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

podcast_url = ''
if not os.path.exists('podcast.mp3'):
  print('getting podcast')
  response = requests.get(podcast_url)

  with open('podcast.mp3', 'wb') as f:
      f.write(response.content)

print('loading audio')
audio = AudioSegment.from_mp3('podcast.mp3')
# OR
# audio = AudioSegment.from_file('session.mkv', 'aac')
transcript = ''

# Chunk duration in milliseconds
chunk_duration_ms = 5 * 60 * 1000
audio_length_ms = len(audio)
num_chunks = int(audio_length_ms / chunk_duration_ms)

for i in range(num_chunks):
    start_time = i * chunk_duration_ms
    end_time = min((i + 1) * chunk_duration_ms, audio_length_ms)
    chunk = audio[start_time:end_time]

    # write the chunk to a temp file
    with tempfile.NamedTemporaryFile(suffix='.mp3', delete=False) as f:
        chunk.export(f.name, format='mp3')
        temp_file_path = f.name
        audio_file = open(temp_file_path, "rb")

    # use the temp file in transcription
    print('transcribing chunk', i)
    transcript += openai.Audio.transcribe(
        file=audio_file,
        model="whisper-1",
        # add the previous transcript as context for better results
        prompt=transcript
    )['text']

    os.remove(temp_file_path)

with open('transcript.txt', 'w') as f:
    f.write(transcript)
