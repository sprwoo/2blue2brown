from flask import Blueprint, jsonify, request
from app.services.supabase import post_message, get_chat_histories
from app.utils.auth_utils import verify_user_token

chat_bp = Blueprint("chat", __name__)

@chat_bp.route("/send_message", methods=["POST"])
def route_send_message():
    user, token_or_error = verify_user_token()
    if user is None:
        return jsonify({"error": token_or_error}), 401

    data = request.json
    chat_session_id = data.get('chat_session_id')
    sender = data.get('sender')
    message = data.get('message')

    if not all([chat_session_id, sender, message]):
        return jsonify({"error": "chat_session_id, sender, and message are required"}), 400

    result = post_message(sender, message, token_or_error)
    return jsonify(result), 200

@chat_bp.route("/get_chat_histories", methods=["GET"])
def route_chat_histories():
    user, token_or_error = verify_user_token()
    if user is None:
        return jsonify({"error": token_or_error}), 401

    session_id = request.args.get("session_id")
    if not session_id:
        return jsonify({"error": "Session ID is required"}), 400

    data = get_chat_histories(session_id, token_or_error)
    return jsonify(data)
