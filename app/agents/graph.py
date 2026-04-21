from langgraph.graph import StateGraph, END
from app.schemas.state import AuditState 
from .deep_harness import planning_node, knowledge_retrieval_node

workflow = StateGraph(AuditState)

workflow.add_node("planner", planning_node)
workflow.add_node("researcher", knowledge_retrieval_node)

workflow.set_entry_point("planner")
workflow.add_edge("planner", "researcher")
workflow.add_edge("researcher", END)

# This 'app' is the workable engine
audit_engine = workflow.compile()