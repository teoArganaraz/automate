from agent.agent import researcher
from pydantic import BaseModel
from fastapi import FastAPI

app = FastAPI()


class Query(BaseModel):
    query: str


@app.post("/")
def researchAgent(query: Query):
    query = query.query
    content = researcher({"input": query})
    actual_content = content['output']
    return actual_content