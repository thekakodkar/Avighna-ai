from langgraph.graph import StateGraph, END
from app.schemas.state import AuditState
from .deep_harness import planning_node, knowledge_retrieval_node

# 1. Initialize the Graph with our State (the shared notepad)
workflow = StateGraph(AuditState)

# 2. Add the nodes from your deep_harness.py
workflow.add_node("planner", planning_node)
workflow.add_node("researcher", knowledge_retrieval_node)

# 3. Define the Flow
workflow.set_entry_point("planner")
workflow.add_edge("planner", "researcher")
workflow.add_edge("researcher", END)

# 4. Compile the engine for main.py
audit_engine = workflow.compile()