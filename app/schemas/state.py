from typing import TypedDict, List, Annotated
from pydantic import BaseModel

class AuditState(TypedDict):
    """The durable state of the Infor audit process."""
    raw_input: str
    plan: List[str]          # Created by the 'Deep' Planning node
    erp_data: dict
    audit_results: dict
    status: str              # 'planning', 'auditing', 'complete'