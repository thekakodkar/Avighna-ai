from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

# This is your 'Guardrail' - the Pydantic Schema
class PurchaseOrder(BaseModel):
    po_id: str = Field(pattern=r"^PO-\d{5}$") # Example: PO-12345
    amount: float
    vendor: str

@app.post("/validate-po")
async def validate_po(po: PurchaseOrder):
    return {"status": "Validated", "data": po}