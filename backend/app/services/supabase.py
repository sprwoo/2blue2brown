import os
import requests
from dotenv import load_dotenv

load_dotenv()

SUPABASE_URL = os.getenv('supaurl')
SUPABASE_ANON_KEY = os.getenv('supakey')

def get_chat_session(uuid):
    try:
        url = f"{SUPABASE_URL}/rest/v1/chat_sessions?id=eq.{uuid}"
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Accept-Profile': 'chatbotschema',
            'apikey': SUPABASE_ANON_KEY
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": response.text}
    except Exception as error:
        return {"error": str(error)}


def get_latest_chat_session():
    try:
        url = f"{SUPABASE_URL}/rest/v1/chat_sessions?order=time_created.desc&limit=1"
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Accept-Profile': 'chatbotschema',
            'apikey': SUPABASE_ANON_KEY
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": response.text}
    except Exception as error:
        return {"error": str(error)}


def get_all_chat_sessions():
    try:
        url = f"{SUPABASE_URL}/rest/v1/chat_sessions?order=time_created.desc"
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Accept-Profile': 'chatbotschema',
            'apikey': SUPABASE_ANON_KEY
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
        url = f"{SUPABASE_URL}/rest/v1/chat_messages?chat_session_id=eq.{session_id}&order=time_created.asc"
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Accept-Profile': 'chatbotschema',
            'apikey': SUPABASE_ANON_KEY
        }


        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": response.text}
    except Exception as error:
        return {"error": str(error)}


def post_chat_session(session_title):
    try:
        url = f"{SUPABASE_URL}/rest/v1/chat_sessions"
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Content-Profile': 'chatbotschema',
            'apikey': SUPABASE_ANON_KEY
        }
        data = {"title": session_title}
        response = requests.post(url, headers=headers, json=data)
        if response.status_code == 201:
            return {"success": "Session created successfully!", "data": response.json()}
        else:
            return {"error": response.text}
    except Exception as error:
        return {"error": str(error)}


def post_message(sender, message, chat_session_id, image_url=None, manim_code=None, image_summary=None):
    try:
        url = f"{SUPABASE_URL}/rest/v1/chat_messages"
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Content-Profile': 'chatbotschema',
            'apikey': SUPABASE_ANON_KEY
        }
        data = {
            "sender": sender,
            "message": message,
            "chat_session_id": chat_session_id,
            "image_url": image_url,
            "manim_code": manim_code,
            "image_summary": image_summary
        }
        response = requests.post(url, headers=headers, json=data)
        if response.status_code == 201:
            return {"success": "Message sent successfully!", "data": response.json()}
        else:
            return {"error": response.text}
    except Exception as error:
        return {"error": str(error)}
