from langchain import OpenAI, LLMChain
from langchain import PromptTemplate
from langchain.memory import ConversationBufferWindowMemory
from dotenv import find_dotenv, load_dotenv
import os
import openai

load_dotenv(find_dotenv())

openai.api_key = os.getenv("OPENAI_API_KEY")

def get_ai_response(human_input):

    template = """
    You are as a role of an AI assistant, now lets playing the following requirements:
    1/ Your Name is Sofia, you are really devoted to help others to achive his goals.
    2/ Your like to use the Polya Heuristics and the Feynman technique in order to solve problems

    {history}
    Person: {human_input}
    Sofia: 
    """
    prompt = PromptTemplate(
        input_variables = {"history","human_input"},
        template = template
    )

    chatgpt_chain = LLMChain(
        llm=OpenAI(temperature = 0),
        prompt = prompt,
        verbose = True,
        memory = ConversationBufferWindowMemory(k=2)

    )

    output = chatgpt_chain.predict(human_input=human_input)

    return output

