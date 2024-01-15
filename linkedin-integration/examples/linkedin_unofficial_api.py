from linkedin_api import Linkedin
from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv())

LINKEDIN_USER_EMAIL = os.getenv("LINKEDIN_USER_EMAIL")
LINKEDIN_USER_PASSWORD = os.getenv("LINKEDIN_USER_PASSWORD")

# Authenticate using any Linkedin account credentials
api = Linkedin(LINKEDIN_USER_EMAIL, LINKEDIN_USER_PASSWORD)

# GET a profile
profile = api.get_profile('user_id')

# Send a message
status = api.send_message(message_body="Hello World!",
                          recipients=[api.get_profile("user_id").get("profile_urn")])


if __name__ == "__main__":
    if status != True:
        print("El mensaje fue enviado exitosamente!")