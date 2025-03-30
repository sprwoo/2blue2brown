from flask import Blueprint, jsonify, request
from app.services.supabase import (
    get_chat_session,
    get_all_chat_sessions,
    get_latest_chat_session
)

session_bp = Blueprint("session", __name__)

@session_bp.route("/", methods=["GET"])
def index():
    return jsonify({"message": "Welcome to the Chatbot API!"})

@session_bp.route("/get_chat_session", methods=["GET"])
def route_chat_session():
    uuid = request.args.get("uuid")
    if not uuid:
        return jsonify({"error": "UUID is required"}), 400

    data = get_chat_session(uuid)
    return jsonify(data[0]) if isinstance(data, list) and data else jsonify({"error": "Session not found"}), 404

@session_bp.route("/get_all_chat_sessions", methods=["GET"])
def route_all_chat_sessions():
    data = get_all_chat_sessions()
    return jsonify(data)

@session_bp.route("/get_latest_session", methods=["GET"])
def route_latest_chat_session():
    data = get_latest_chat_session()
    if isinstance(data, list) and data:
        return jsonify(data[0])
    elif isinstance(data, list):
        return jsonify({"error": "No sessions found"}), 404
    else:
        return jsonify(data)
    
@session_bp.route("/post_chat_session", methods=["POST"])
def route_post_chat_session():
    data = request.json

    # We need the user_id, so update this as soon as we figure out user_id
    # user_id = data.get('user_id', 'NULL')
    session_title = data.get('session_title', 'NULL')

    # if user_id == 'NULL':
    #     return jsonify({"error": "User ID is required"}), 400

    # result = post_chat_session(user_id, session_title)
    result = post_chat_session(session_title)
    return jsonify(result), 200