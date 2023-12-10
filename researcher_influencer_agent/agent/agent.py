from langchain import OpenAI, LLMChain
from langchain import PromptTemplate
from langchain.document_loaders import UnestructuredURLLoader
from langchain.text_splitter import CharacterTextSplitter
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
    
    return url_list

def get_content_from_urls(urls):
    
    loader = UnestructuredURLLoader(urls=urls)
    
    data = loader.load()
    
    return data

def generate_summary(data,query):
    text_splitter = CharacterTextSplitter(separator="\n", chunk_size=3000, chunl_overlap=200, lenght_function=len)

    llm = OpenAI(model_name = "gpt-3.5-turbo", temperature=.2)
    template = """
    {text}
    You are a Word Class Journalist and Researcher, you will try to summarize the text above about {query}

    Please follow all the following instructions:

    INSTRUCTIONS
    //.1 Make sure the content is engaging, informative, with good data.
    //.2 Make sure the content is not too long, it should be no more than 3-5 tweets
    //.3 The content should adress the {query} topic very well
    //.4 The content needs to be written in a way that is easy to read and understand.
    //.5 The content needs to give audience actionable advice and insights too.

    SUMMARY:
    """

    prompt_template = PromptTemplate(
        input_variables = ["text","query"],template = template)
    
    summarizer_chain = LLMChain(llm=llm,
                                prompt=prompt_template,
                                verbose=True)
    
    summaries = []

    for chunk in enumerate(data):
        summary = summarizer_chain.predict(text=chunk,query=query)
        summaries.append(summary)

    return summaries


def generate_post(summaries,query):
    summaries_str = str(summaries)

    llm = OpenAI(model_name = "gpt-3.5-turbo", temperature=.7)
    template = """
    {text}
    You are a Word Class Journalist, Writer, and Influencer. The text above is some content about {query}

    Please write a viral twitter thread about {query} using the text above and following the instructions below:

    INSTRUCTIONS
    //.1 Make a post engaging, informative, with good data.
    //.2 Make sure the post is not too long, it should be no more than 3-5 tweets
    //.3 The post should adress the {query} topic very well
    //.4 The post needs to be written in a way that is easy to read and understand.
    //.5 The post needs to give audience actionable advice and insights too.
    //.6 The post needs to be viral, and get at least 1000 likes.

    POST:
    """

    prompt_template = PromptTemplate(
        input_variables = ["summaries_str","query"],template = template)
    
    post_chain = LLMChain(llm=llm,
                          prompt=prompt_template,
                          verbose=True)
    
    text_post = post_chain.predic(summaries_str=summaries_str,query=query)

    return text_post