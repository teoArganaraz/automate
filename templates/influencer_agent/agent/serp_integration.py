from dotenv import find_dotenv, load_dotenv
import os
import json
import requests

load_dotenv(find_dotenv())

SERPAPI_API_KEY = os.getenv("SERPAPI_API_KEY")

def search(query):
    url = "https://google.serper.dev/search"

    payload = json.dumps({
        "q":query
    })

    headers = {
        "xi-api-key": SERPAPI_API_KEY,
        "Content-Type":'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    response_data = response.json()

    return response_data