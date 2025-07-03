from fastapi import FastAPI
from app.api import router

app = FastAPI(
    title="LangGraph Multi-Agent Backend",
    description="An API to run multi-agent workflows powered by LangGraph + Groq",
    version="1.0.0"
)

app.include_router(router)