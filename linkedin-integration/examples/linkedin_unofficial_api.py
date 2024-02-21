from linkedin_api import Linkedin
from dotenv import load_dotenv, find_dotenv
import os
import json

load_dotenv(find_dotenv())

LINKEDIN_USER_EMAIL = os.getenv("LINKEDIN_USER_EMAIL")
LINKEDIN_USER_PASSWORD = os.getenv("LINKEDIN_USER_PASSWORD")

# Authenticate using any Linkedin account credentials
api = Linkedin(LINKEDIN_USER_EMAIL, LINKEDIN_USER_PASSWORD)

id = "public_id"
urn = "profile_urn"
conversation_urn = "conversation_urn"

# GET a profile
profile = api.get_profile(id)
conversations = api.get_conversations()
conversation = api.get_conversation(conversation_urn)
last_message = api.get_conversation_details(urn)

# Serializing json
json_object = json.dumps(profile)
json_conversations = json.dumps(conversations)
json_conversation = json.dumps(conversation)
json_last_message = json.dumps(last_message)
 
# Writing to sample.json
with open(f".\examples\profile_{id}.json", "w") as outfile:
    outfile.write(json_object)

with open(".\examples\conversations.json", "w") as outfile:
    outfile.write(json_conversations)

with open(f".\examples\conversation_{conversation_urn}.json", "w") as outfile:
    outfile.write(json_conversation)

with open(f".\examples\last_message_{id}.json", "w") as outfile:
    outfile.write(json_last_message)

