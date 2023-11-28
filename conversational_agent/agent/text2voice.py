import requests
from playsound import playsound
import os

ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")
ELEVENLABS_URL = ""

def get_tts_elevenlabs(message):
    payload = {
        "text" : message,
        "model" : "elevenlabs_monolingual_v1",
        "voice_settings":{
            "stability":0,
            "similarity_boost":0
        }
    }

    headers = {
        "accept" : "audio/mpeg",
        "xi-api-key": ELEVENLABS_API_KEY,
        "Content-Type":'application/json'
    }

    response = requests.post(ELEVENLABS_URL, json=payload, headers=headers)

    if response.status_code == 200 and response.content:
        with open("audio.mp3", 'wb') as f:
            f.write(response.content)
        playsound("audio.mp3")
        return response.content