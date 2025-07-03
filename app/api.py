from fastapi import APIRouter
from pydantic import BaseModel
from app.core.workflow import graph
from langchain_core.messages import HumanMessage

router = APIRouter()

class QueryRequest(BaseModel):
    query: str

@router.post("/run-task")
def run_task(payload: QueryRequest):
    task = payload.query.strip()
    inputs = {
        "messages": [HumanMessage(content=task)],
        "current_task": task
    }

    final_state = graph.invoke(inputs)
    return {
        "report": final_state.get("final_report", "No report generated."),
        "status": "success"
    }