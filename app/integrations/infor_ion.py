import httpx

async def get_po_from_erp(po_number: str):
    """MOCK FUNCTION: Replace with your actual Infor ION credentials."""
    # In reality, you would use your .env credentials to get an OAuth token first.
    # For testing, we return a mock object that looks like Infor data.
    return {
        "po_number": po_number,
        "erp_price": 100.0,
        "item": "CNC-Widget-01"
    }