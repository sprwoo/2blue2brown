import os
import requests
from dotenv import load_dotenv
from flask import Flask, jsonify, request
from flask_cors import CORS

load_dotenv()

SUPABASE_URL = os.getenv('supaurl')
SUPABASE_ANON_KEY = os.getenv('supakey')

app = Flask(__name__)
CORS(app)

def get_test():
    try:
        url = f"{SUPABASE_URL}/rest/v1/chat_messages?"
        
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'apikey': SUPABASE_ANON_KEY,
            'Authorization': f'Bearer {SUPABASE_ANON_KEY}',
            'Accept-Profile': 'chatbotschema'
        }
        
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": response.text}
    
    except Exception as error:
        return {"error": str(error)}

def post_test(sender, message):
    try:
        url = f"{SUPABASE_URL}/rest/v1/chat_messages?"
        
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'apikey': SUPABASE_ANON_KEY,
            'Authorization': f'Bearer {SUPABASE_ANON_KEY}',
            'Content-Profile': 'chatbotschema'
        }
        
        data = {
            "sender": sender,
            "message": message
        }
        
        response = requests.post(url, headers=headers, json=data)
        if response.status_code == 201:
            return {"success": "Data posted successfully!", "data": response.json()}
        else:
            return {"error": response.text}
    
    except Exception as error:
        return {"error": str(error)}

def get_chat_sessions(uuid):
    try:
        url = f"{SUPABASE_URL}/rest/v1/chat_sessions?title=eq.{uuid}"
        
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'apikey': SUPABASE_ANON_KEY,
            'Authorization': f'Bearer {SUPABASE_ANON_KEY}',
            'Accept-Profile': 'chatbotschema'
        }

        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": response.text}
    
    except Exception as error:
        return {"error": str(error)}

def get_chat_histories(session_id):
    try:
        url = f"{SUPABASE_URL}/rest/v1/chat_messages?message=eq.{session_id}&order=time.asc"
        
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'apikey': SUPABASE_ANON_KEY,
            'Authorization': f'Bearer {SUPABASE_ANON_KEY}',
            'Accept-Profile': 'chatbotschema'
        }

        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": response.text}
    except Exception as error:
        return {"error": str(error)}

def post_message(sender, message):
    try:
        url = f"{SUPABASE_URL}/rest/v1/chat_messages?"
        
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'apikey': SUPABASE_ANON_KEY,
            'Authorization': f'Bearer {SUPABASE_ANON_KEY}',
            'Content-Profile': 'chatbotschema'
        }
        
        data = {
            "sender": sender,
            "message": message
        }
        
        response = requests.post(url, headers=headers, json=data)
        if response.status_code == 201:
            return {"success": "Message sent successfully!", "data": response.json()}
        else:
            return {"error": response.text}
    
    except Exception as error:
        return {"error": str(error)}

@app.route("/api", methods=["GET"])
def home():
    return jsonify({"message": "Hello from Flask!"})

@app.route("/api/get_test", methods=["GET"])
def api_get_test():
    result = get_test()

    return jsonify(result)

@app.route("/api/post_test", methods=["POST"])
def api_post_test():
    data = request.json
    sender = data.get('sender', 'user')  
    message = data.get('message', 'No message provided')
    result = post_test(sender, message)

    return jsonify(result)

@app.route("/api/get_chat_sessions", methods=["GET"])
def route_chat_sessions():
    uuid = request.args.get("uuid")  # Get the UUID from query params
    if not uuid:
        return jsonify({"error": "UUID is required"}), 400

    data = get_chat_sessions(uuid)
    return jsonify(data)

@app.route("/api/get_chat_histories", methods=["GET"])
def route_chat_histories():
    session_id = request.args.get("session_id")  # Get the session_id from query params
    if not session_id:
        return jsonify({"error": "Session ID is required"}), 400

    data = get_chat_histories(session_id)
    return jsonify(data)

@app.route("/api/send_message", methods=["POST"])
def route_send_message():
    data = request.json
    chat_session_id = data.get('chat_session_id', 'NULL')
    if chat_session_id == 'NULL':
        return jsonify({"error": "Chat session ID is required"}), 400
    
    sender = data.get('sender', 'NULL')  
    message = data.get('message', 'NULL')

    result = post_message(sender, message)
    return jsonify(result), 200

if __name__ == "__main__":
    app.run(debug=True, port=5001)
