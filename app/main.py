from fastapi import FastAPI
from app.agents.graph import audit_engine

app = FastAPI(title="Infor LN Sidecar")

@app.post("/start-audit")
async def start_audit(email_content: str):
    # Triggers the deep agentic flow
    final_state = await audit_engine.ainvoke({"raw_input": email_content})
    return final_state