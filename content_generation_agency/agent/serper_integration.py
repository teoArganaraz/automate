import requests
import json
from dotenv import load_dotenv
import os

load_dotenv()
serper_api_key = os.getenv("SERP_API_KEY")

def search(query):
    url = "https://google.serper.dev/search"

    payload = json.dumps({
        "q": query
    })

    headers = {
        'X-API-KEY': serper_api_key,
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    return response.text