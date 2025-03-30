from langgraph.graph import StateGraph, END
from typing import TypedDict

from app.langgraph_nodes import (
    load_context,
    should_generate_video,
    chat_response,
    generate_script_chunks,
    generate_clips,
)

class GraphState(TypedDict, total=False):
    user_input: str
    session_id: str
    chat_summary: str 
    chat_history: list 
    make_video: bool 
    scene_plan: list
    code_chunks: list

def build_graph():
    graph = StateGraph(GraphState)

    graph.add_node("load_context", load_context)
    graph.add_node("decision_node", should_generate_video)
    graph.add_node("chat_response_node", chat_response)
    graph.add_node("director_node", generate_script_chunks)
    graph.add_node("clip_agents_node", generate_clips)

    graph.set_entry_point("load_context")
    graph.add_edge("load_context", "decision_node")

    # Conditional branching
    graph.add_conditional_edges(
        "decision_node",
        lambda state: "director_node" if state.get("make_video") else "chat_response_node"
    )

    # End either after director or chat response for now
    graph.add_edge("chat_response_node", END)
    graph.add_edge("director_node", "clip_agents_node")
    graph.add_edge("clip_agents_node", END)

    return graph.compile()