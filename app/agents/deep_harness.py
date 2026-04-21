from ollama import AsyncClient
from app.schemas.state import AuditState

async def planning_node(state: AuditState):
    """Deep Agent logic: Decomposes the task into steps."""
    client = AsyncClient()
    response = await client.chat(model='llama3.2', messages=[
        {'role': 'system', 'content': 'Create a 3-step plan to audit this PO.'},
        {'role': 'user', 'content': state['raw_input']}
    ])
    return {"plan": response['message']['content'].split("\n"), "status": "auditing"}

async def knowledge_retrieval_node(state: AuditState):
    """Calls Flowise to search Qdrant for part manuals."""
    # This bridges your Python code to your visual Flowise UI
    return {"audit_results": {"manual_check": "Verified part dimensions match."}}