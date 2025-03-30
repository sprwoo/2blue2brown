from flask import Blueprint, jsonify, request
from app.services.supabase import (
    get_chat_session,
    get_all_chat_sessions,
    get_latest_chat_session
)
from app.utils.auth_utils import verify_user_token

session_bp = Blueprint("session", __name__)

@session_bp.route("/asd", methods=["GET"])
def index():
    return jsonify({"message": "Welcome to the Chatbot API!"})

@session_bp.route("/get_chat_session", methods=["GET"])
def route_chat_session():
    user, token_or_error = verify_user_token()
    if user is None:
        return jsonify({"error": token_or_error}), 401

    uuid = request.args.get("uuid")
    if not uuid:
        return jsonify({"error": "UUID is required"}), 400

    data = get_chat_session(uuid, token_or_error)
    return jsonify(data[0]) if isinstance(data, list) and data else jsonify({"error": "Session not found"}), 404

@session_bp.route("/get_all_chat_sessions", methods=["GET"])
def route_all_chat_sessions():
    user, token_or_error = verify_user_token()
    if user is None:
        return jsonify({"error": token_or_error}), 401

    data = get_all_chat_sessions(token_or_error)
    return jsonify(data)

@session_bp.route("/get_latest_session", methods=["GET"])
def route_latest_chat_session():
    user, token_or_error = verify_user_token()
    if user is None:
        return jsonify({"error": token_or_error}), 401

    data = get_latest_chat_session(token_or_error)
    if isinstance(data, list) and data:
        return jsonify(data[0])
    elif isinstance(data, list):
        return jsonify({"error": "No sessions found"}), 404
    else:
        return jsonify(data)
