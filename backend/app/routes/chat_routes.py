from flask import Blueprint, jsonify, request
from app.services.supabase import post_message, get_chat_histories

chat_bp = Blueprint("chat", __name__)

@chat_bp.route("/send_message", methods=["POST"])
def route_send_message():
    data = request.json
    chat_session_id = data.get('chat_session_id', 'NULL')
    if chat_session_id == 'NULL':
        return jsonify({"error": "Chat session ID is required"}), 400
    
    sender = data.get('sender', 'NULL')  
    message = data.get('message', 'NULL')

    result = post_message(sender, message)
    return jsonify(result), 200

@chat_bp.route("/get_chat_histories", methods=["GET"])
def route_chat_histories():
    session_id = request.args.get("session_id")  
    if not session_id:
        return jsonify({"error": "Session ID is required"}), 400

    data = get_chat_histories(session_id)
    return jsonify(data)