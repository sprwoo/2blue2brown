from flask import Blueprint, jsonify, request
from app.services.supabase import post_message, get_chat_histories
import json

chat_bp = Blueprint("chat", __name__)

@chat_bp.route("/send_message", methods=["POST"])
def route_send_message():
    data = request.json
    chat_session_id = data.get('chat_session_id')
    sender = data.get('sender')
    message = data.get('message')

    if not all([chat_session_id, sender, message]):
        return jsonify({"error": "chat_session_id, sender, and message are required"}), 400

    result = post_message(sender, message)
    return jsonify(result), 200


@chat_bp.route("/get_chat_histories", methods=["GET"])
def route_chat_histories():
    chat_session_id = request.args.get("chat_session_id")
    if not chat_session_id:
        return jsonify({"error": "Missing chat_session_id parameter"}), 400

    try:
        # Query chat histories using chat_session_id
        result = get_chat_histories(chat_session_id)

        for row in result:
            print(row)

        # print("Raw result:", result)  # Debug: print raw result

        # # If your service returns an object with a data field, extract it:
        # history = result.get("data", result)

        # messages = []
        # for row in history:
        #     # If row is a string, attempt to parse it.
        #     if isinstance(row, str):
        #         row = row.strip() and json.loads(row) or {}
        #     messages.append(row)
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@chat_bp.route("/chat", methods=["POST"])
def handle_chat():
    from app.controllers import build_graph
    data = request.get_json()
    user_input = data.get("user_input")
    session_id = data.get("session_id")
    print(user_input, session_id)
    return jsonify({
        "status": "success",
        "echo": {
            "user_input": user_input,
            "session_id": session_id
        }
    })
    # graph = build_graph()
    
    # state = {
    #     "user_input": user_input,
    #     "session_id": session_id,
    # }
    # result = graph.invoke(state)
    
    # if result.get("make_video"):
    #     return jsonify({
    #         "code_chunks": result.get("code_chunks", []),
    #         "message": "Generated animation code.",
    #     })
    # else:
    #     return jsonify({
    #         "response": result.get("chat_response"),
    #         "message": "Text response only.",
    #     })
        
