"""
Here is an example of using the client to make a simple GET request to fetch the current user's information.
This requires a 3-legged access token with the "openid" and "profile" scope, which is included with the
Sign In With LinkedIn using OpenID Connect API product.
"""

from linkedin_api.clients.restli.client import RestliClient
from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv())

ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
restli_client = RestliClient()

response = restli_client.get(
  resource_path="/userinfo",
  access_token=ACCESS_TOKEN
)

#print(response.entity)

if __name__ == "__main__":
  print(response.entity)