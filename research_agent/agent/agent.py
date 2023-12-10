from langchain import OpenAI, LLMChain
from langchain import PromptTemplate
import openai
import json
from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv())

SERPAPI_API_KEY = os.getenv("SERPAPI_API_KEY")
openai.api_key = os.getenv("OPENAI_API_KEY")

def find_relevant_articles_urls(response_data, query):

    response_str = json.dumps(response_data)

    llm = OpenAI(model_name = "gpt-3.5-turbo", temperature=.5)
    template = """
    You are a Word Class Journalist and Researcher, you are extremly good at find the most relevant articles to certain topic;
    {response_str}
    Above is the of search results for the query {query}
    Please choose the best 3 articles from the list, return ONLY an array with the urls, do not include anything else;
    """

    prompt_template = PromptTemplate(
        input_variables = ["response_str","query"],template = template)
    
    article_picker_chain = LLMChain(llm=llm,
                                    prompt=prompt_template,
                                    verbose=True)
    
    urls = article_picker_chain.predict(response_str=response_str,query=query)

    url_list = json.loads(urls)
