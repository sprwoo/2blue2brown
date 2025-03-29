from app.controllers import build_graph

@app.route("/chat", methods=["POST"])
def handle_chat():
    data = request.get_json()
    user_input = data.get("user_input")
    session_id = data.get("session_id")
    
    graph = build_graph()
    
    state = {
        "user_input": user_input,
        "session_id": session_id,
    }
    result = graph.invoke(state)
    
    if result.get("make_video"):
        return jsonify({
            "code_chunks": result.get("code_chunks", []),
            "message": "Generated animation code.",
        })
    else:
        return jsonify({
            "response": result.get("chat_response"),
            "message": "Text response only.",
        })
        