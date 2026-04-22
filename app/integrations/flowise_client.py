import httpx

FLOWISE_URL = "http://localhost:3000/api/v1/prediction/"
FLOW_ID = "FLOW_ID"

async def query_knowledge_base(question: str):
    """Sends a question to Flowise and gets the answer from the manual."""
    async with httpx.AsyncClient() as client:
        payload = {"question": question}
        response = await client.post(f"{FLOWISE_URL}{FLOW_ID}", json=payload)
        # Flowise usually returns {'text': 'The answer...'}
        return response.json().get("text")