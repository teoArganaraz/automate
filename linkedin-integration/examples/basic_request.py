from linkedin_api.clients.restli.client import RestliClient
from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv())

ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
restli_client = RestliClient()

response = restli_client.get(
  resource_path="/me",
  access_token=ACCESS_TOKEN
)

#print(response.entity)

if __name__ == "__main__":
  print(response.entity)
