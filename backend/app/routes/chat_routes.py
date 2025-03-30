from flask import Blueprint, jsonify, request
from app.services.supabase import post_message, get_chat_histories
import json
from app.controllers import Chunky

chat_bp = Blueprint("chat", __name__)

# @chat_bp.route("/send_message", methods=["POST"])
# def route_send_message():
#     data = request.json
#     chat_session_id = data.get('chat_session_id')
#     sender = data.get('sender')
#     message = data.get('message')

#     if not all([chat_session_id, sender, message]):
#         return jsonify({"error": "chat_session_id, sender, and message are required"}), 400

#     result = post_message(sender, message)
#     return jsonify(result), 200


@chat_bp.route("/get_chat_histories", methods=["GET"])
def route_chat_histories():
    chat_session_id = request.args.get("chat_session_id")
    if not chat_session_id:
        return jsonify({"error": "Missing chat_session_id parameter"}), 400

    try:
        result = get_chat_histories(chat_session_id)

        for row in result:
            print(row)
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@chat_bp.route("/chat", methods=["POST"])
def handle_chat():
    from app.controllers import build_graph
    user_input = request.form.get("user_input")
    session_id = request.form.get("session_id")

    image_summary = None
    if "image" in request.files:
        image_file = request.files["image"]
        if image_file.filename != "":
            file_bytes = image_file.read()
            chunky = Chunky()
            image_summary = chunky.advanced_image_handling(user_input, file_bytes)
            print("image summary", image_summary)
        
    # graph = build_graph()
    
    # state = {
    #     "user_input": user_input,
    #     "session_id": session_id,
    # }
    # result = graph.invoke(state)
    
    # # we'll now save the user and ai messages
    # chat_session_id = session_id
    # sender = "user"
    # message = user_input
    # post_status = post_message(sender, message, chat_session_id)
    
    # sender = "ai"
    # message = result.get("chat_response")
    # manim_code = "\n".join(result.get("code_chunks", [])) or None
    # post_status = post_message(sender, message, chat_session_id, manim_code=manim_code)
    
    return jsonify({
        "status": "success",
        "echo": {
            "user_input": user_input,
            "session_id": session_id
        }
    })
        
