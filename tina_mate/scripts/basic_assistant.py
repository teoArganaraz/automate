from openai import OpenAI
import openai
from tenacity import retry, wait_random_exponential, stop_after_attempt
from termcolor import colored  
from typing import Dict, List
from utilities import prompts, tools
from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv())

LINKEDIN_USER_EMAIL = os.getenv("LINKEDIN_USER_EMAIL")
LINKEDIN_USER_PASSWORD = os.getenv("LINKEDIN_USER_PASSWORD")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

GPT_MODEL = "gpt-4"

client = OpenAI()
openai.api_key = OPENAI_API_KEY

@retry(wait=wait_random_exponential(multiplier=1, max=40), stop=stop_after_attempt(3))
def chat_completion_request(messages, tools=None, tool_choice=None, model=GPT_MODEL):
    try:
        response = client.chat.completions.create(
            model=model,
            messages=messages,
            tools=tools,
            tool_choice=tool_choice,
        )
        return response
    except Exception as e:
        print("Unable to generate ChatCompletion response")
        print(f"Exception: {e}")
        return e
    

    
def pretty_print_conversation(messages):
    role_to_color = {
        "system": "red",
        "user": "green",
        "assistant": "blue",
        "function": "magenta",
    }
    
    for message in messages:
        if message["role"] == "system":
            print(colored(f"system: {message['content']}\n", role_to_color[message["role"]]))
        elif message["role"] == "user":
            print(colored(f"user: {message['content']}\n", role_to_color[message["role"]]))
        elif message["role"] == "assistant" and message.get("function_call"):
            print(colored(f"assistant: {message['function_call']}\n", role_to_color[message["role"]]))
        elif message["role"] == "assistant" and not message.get("function_call"):
            print(colored(f"assistant: {message['content']}\n", role_to_color[message["role"]]))
        elif message["role"] == "function":
            print(colored(f"function ({message['name']}): {message['content']}\n", role_to_color[message["role"]]))


messages = []
messages.append({"role": "system", "content": prompts.get("basic_assistant_prompt")})
messages.append({"role": "user", "content": prompts.get("teo2max_prompt")})

print(messages)

if __name__=="__main__":
    chat_response = chat_completion_request(
    messages, tools=tools)
    print(chat_response.choices[0].message.content)