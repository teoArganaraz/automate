# Installation

1. Create a python enviroment (python-version==3.9.1)
2. pip install `requirements.txt`

# Tina Mate

## Message Scope

### Structure

This folder contains three scripts:

- `utilities.py`: This script contains the definitions and tools used by the basic assistant.
- `basic_assistant.py`: This is an assistant that utilizes the chat completion API of OpenAI to create opening messages based on prompt instructions.
- `send_message.py`: This module is responsible for sending messages created by the basic assistant via LinkedIn.

### Description

The following scripts demonstrate a basic connection between the unofficial LinkedIn API and the OpenAI API, but they have several limitations:

- They do not maintain conversation threads.
- They only generate opening messages.
- They log in to LinkedIn every time a message is sent.
- They do not utilize any tools defined in `utilities.py`.

## Campaign Scope

Pending
