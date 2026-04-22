from ollama import AsyncClient
import httpx
from app.schemas.state import AuditState

# Replace with your actual Flowise Flow ID from the UI
FLOWISE_API_URL = "http://localhost:3000/api/v1/prediction/YOUR_FLOW_ID"

async def planning_node(state: AuditState):
    """Deep Agent logic: Decomposes the task into steps."""
    print("--- STEP 1: PLANNING ---")
    client = AsyncClient()
    response = await client.chat(model='llama3.2', messages=[
        {'role': 'system', 'content': 'Create a concise 3-step plan to audit this Infor LN Purchase Order.'},
        {'role': 'user', 'content': state['raw_input']}
    ])
    # Extracting the text response and splitting into a list
    plan_text = response['message']['content']
    return {"plan": plan_text.split("\n"), "status": "planning_complete"}

async def knowledge_retrieval_node(state: AuditState):
    """Bridges Python to Flowise to search Qdrant manuals."""
    print("--- STEP 2: KNOWLEDGE RETRIEVAL (FLOWISE) ---")
    
    # This is the actual call to your Flowise visual chain
    async with httpx.AsyncClient() as client:
        payload = {"question": f"Extract part specifications for the items mentioned in: {state['raw_input']}"}
        try:
            response = await client.post(FLOWISE_API_URL, json=payload, timeout=30.0)
            flowise_data = response.json().get("text", "No manual data found.")
        except Exception as e:
            flowise_data = f"Flowise Connection Error: {str(e)}"

    return {"audit_results": {"manual_check": flowise_data}, "status": "research_complete"}