from linkedin_api import Linkedin
from dotenv import load_dotenv, find_dotenv
import os
from typing import List

authenticated = False

load_dotenv(find_dotenv())

LINKEDIN_USER_EMAIL = os.getenv("LINKEDIN_USER_EMAIL")
LINKEDIN_USER_PASSWORD = os.getenv("LINKEDIN_USER_PASSWORD")


def send_linkedin_message(message_body:str,
                          recipients:List[str],
                          user:str=LINKEDIN_USER_EMAIL,
                          password:str=LINKEDIN_USER_PASSWORD,):
    print("empece a correr lo juro")

    global authenticated
    print(authenticated)
    
    if not authenticated:
        print("entre aca")
        api = Linkedin(user, password)
        print(api)
        authenticated = True

    status = api.send_message(message_body=message_body, recipients=recipients)

    if status:
        print("hola")
        print("An error ocurred sending the message")
    else:
        print("The message was sended succesfuly.")


if __name__ ==  "__main__":
    from basic_assistant import chat_completion_request
    from utilities import prompts, tools
    messages = []
    messages.append({"role": "system", "content": prompts.get("basic_assistant_prompt")})
    messages.append({"role": "user", "content": prompts.get("teo2max_prompt")})

    chat_response = chat_completion_request(messages, tools=tools)

    print(send_linkedin_message(chat_response.choices[0].message.content,
                                ["ACoAACMrodEB9G-s6Pckz-OzPBqPq_1Cqlpz49g"]))
