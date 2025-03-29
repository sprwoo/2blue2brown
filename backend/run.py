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

def check_connection():
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

def post_test():
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
            "sender": "user",
            "message": "Hello, World!"
        }
        
        response = requests.post(url, headers=headers, json=data)
        if response.status_code == 201:
            return {"success": "Data posted successfully!", "data": response.json()}
        else:
            return {"error": response.text}
    
    except Exception as error:
        return {"error": str(error)}


@app.route("/api", methods=["GET"])
def home():
    return jsonify({"message": "Hello from Flask!"})

@app.route("/api/check_connection", methods=["GET"])
def api_check_connection():
    result = check_connection()
    return jsonify(result)

@app.route("/api/post_test", methods=["POST"])
def api_post_test():
    result = post_test()
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True, port=5001)
