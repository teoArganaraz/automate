from linkedin_api import Linkedin
from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv())

LINKEDIN_USER_EMAIL = os.getenv("LINKEDIN_USER_EMAIL")
LINKEDIN_USER_PASSWORD = os.getenv("LINKEDIN_USER_PASSWORD")

# Authenticate using any Linkedin account credentials
api = Linkedin(LINKEDIN_USER_EMAIL, LINKEDIN_USER_PASSWORD)

# GET a profile
profile = api.get_profile('max-caceres')

# Send a message
status = api.send_message(message_body="Fue el URN",
                         recipients=["ACoAACMrodEB9G-s6Pckz-OzPBqPq_1Cqlpz49g"])


if __name__ == "__main__":
    print(api.get_conversation_details("ACoAACMrodEB9G-s6Pckz-OzPBqPq_1Cqlpz49g"))