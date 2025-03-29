from langgraph.graph import StateGraph, END

from app.langraph_nodes import (
    load_context,
    should_generate_video,
    chat_response,
    generate_script_chunks,
    generate_clips,
)

def build_graph():
    graph = StateGraph()
    
    graph.add_node("load_context", load_context)
    graph.add_node("decision_node", should_generate_video)
    graph.add_node("chat_response_node", chat_response)
    graph.add_node("director_node", generate_script_chunks) 
    graph.add_node("clip_agents_node", generate_clips)
    
    graph.set_entry_point("load_context")
    graph.add_edge("load_context", "decision_node")
    
    graph.add_conditional_edges(
        "decision_node",
        lambda state: "director_node" if state.get("make_video") else "chat_response_node"
    )
    
    graph.add_edge("director_node", "clip_agents_node")
    graph.add_edge("clip_agents_node", END)
    
    graph.add_edge("chat_response_node", END)
    
    return graph.compile()