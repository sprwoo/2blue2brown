import os
import requests
from dotenv import load_dotenv

load_dotenv()

SUPABASE_URL = os.getenv('supaurl')


def get_chat_session(uuid, user_token):
    try:
        url = f"{SUPABASE_URL}/rest/v1/chat_sessions?id=eq.{uuid}"
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': f'Bearer {user_token}',
            'Accept-Profile': 'chatbotschema'
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": response.text}
    except Exception as error:
        return {"error": str(error)}


def get_latest_chat_session(user_token):
    try:
        url = f"{SUPABASE_URL}/rest/v1/chat_sessions?order=time_created.desc&limit=1"
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': f'Bearer {user_token}',
            'Accept-Profile': 'chatbotschema'
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": response.text}
    except Exception as error:
        return {"error": str(error)}


def get_all_chat_sessions(uuid, user_token):
    try:
        url = f"{SUPABASE_URL}/rest/v1/chat_sessions?id=eq.{uuid}&order=time_created.desc"
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': f'Bearer {user_token}',
            'Accept-Profile': 'chatbotschema'
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": response.text}
    except Exception as error:
        return {"error": str(error)}


def get_chat_histories(session_id, user_token):
    try:
        url = f"{SUPABASE_URL}/rest/v1/chat_messages?chat_session_id=eq.{session_id}&order=time.asc"
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': f'Bearer {user_token}',
            'Accept-Profile': 'chatbotschema'
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": response.text}
    except Exception as error:
        return {"error": str(error)}


def post_chat_session(session_title, user_token):
    try:
        url = f"{SUPABASE_URL}/rest/v1/chat_sessions"
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': f'Bearer {user_token}',
            'Content-Profile': 'chatbotschema'
        }
        data = {"title": session_title}
        response = requests.post(url, headers=headers, json=data)
        if response.status_code == 201:
            return {"success": "Session created successfully!", "data": response.json()}
        else:
            return {"error": response.text}
    except Exception as error:
        return {"error": str(error)}


def post_message(sender, message, user_token):
    try:
        url = f"{SUPABASE_URL}/rest/v1/chat_messages"
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': f'Bearer {user_token}',
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
