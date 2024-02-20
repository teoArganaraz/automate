from linkedin_api import Linkedin
from dotenv import load_dotenv, find_dotenv
import os
import json

load_dotenv(find_dotenv())

LINKEDIN_USER_EMAIL = os.getenv("LINKEDIN_USER_EMAIL")
LINKEDIN_USER_PASSWORD = os.getenv("LINKEDIN_USER_PASSWORD")

# Authenticate using any Linkedin account credentials
api = Linkedin(LINKEDIN_USER_EMAIL, LINKEDIN_USER_PASSWORD)

id = "max-caceres"
urn = "ACoAACMrodEB9G-s6Pckz-OzPBqPq_1Cqlpz49g"
conversation_urn = "2-YWEzMGMwMWItN2U1Ny00MjEyLTg5YTEtY2Y3Njk4YzUzZDQ5XzAxMw=="

# GET a profile
profile = api.get_profile('max-caceres')
conversations = api.get_conversations()
conversation = api.get_conversatio(conversation_urn)
last_message = api.get_conversation_details(urn)

# Serializing json
json_object = json.dumps(profile)
json_conversations = json.dumps(conversations)
json_conversation = json.dumps(conversation)
json_last_message = json.dumps(last_message)
 
# Writing to sample.json
with open(".\linkedin_integration\examples\profile.json", "w") as outfile:
    outfile.write(json_object)

with open(".\linkedin_integration\examples\conversations.json", "w") as outfile:
    outfile.write(json_conversations)

with open(f".\linkedin_integration\examples\conversation_{id}.json", "w") as outfile:
    outfile.write(json_object)

with open(f".\linkedin_integration\examples\last_message_{id}.json", "w") as outfile:
    outfile.write(json_conversations)

