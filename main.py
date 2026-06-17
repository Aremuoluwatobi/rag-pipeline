from fastapi import FastAPI
from pydantic import BaseModel
from retrieval import retrieve_data
from AI_response import ai_response
from ingestion import ingest_pipeline

app = FastAPI(
    title="My Scholar RAG API",
    description="RAG system for academic documents",
    version="1.0.0"
)


class QueryRequest(BaseModel):
    question: str


@app.get("/health")
def health():
    return {"Status: healthy"}


@app.post("/ingest")
def ingestion():
    ingest_pipeline()

    return {"message": "Ingestion complete"}


@app.post("/query")
def query_database(request: QueryRequest):

    context = retrieve_data(request.question)

    response = ai_response(request.question + str(context))

    return {"answer": response}
