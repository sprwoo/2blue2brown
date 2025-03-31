import os
import requests
from dotenv import load_dotenv
import json
from datetime import datetime
import uuid

load_dotenv()

SUPABASE_URL = os.getenv('supaurl')
SUPABASE_ANON_KEY = os.getenv('supakey')

def get_chat_session(uuid):
    try:
        url = f"{SUPABASE_URL}/rest/v1/chat_sessions?id=eq.{uuid}"
        print(url)
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
            'apikey': SUPABASE_ANON_KEY,
            "Authorization": f"Bearer {SUPABASE_ANON_KEY}"
        }
        data = {
            "id" : str(uuid.uuid4()),
            "user_id": None,
            "title": session_title,
            "time_created": datetime.now().isoformat(),
        }
        json_data = json.dumps(data)  
        response = requests.post(url, headers=headers, data=json_data, params={"select": "id"})
        print("Response Content:", response.text)

        if response.status_code == 201:
            # If the session is created successfully, extract and return the 'id'
            session_data = response.json()
            session_id = session_data[0]['id']  # Assuming response contains a list with the created session
            return {"success": "Session created successfully!", "session_id": session_id}
        else:
            # If there is an error, return the error message
            return {"error": response.text}

    except Exception as error:
        return {"error": str(error)}


def post_message(sender, message, chat_session_id, image_url=None, manim_code=None, image_summary=None, video_url=None):
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
            "image_summary": image_summary,
            "video_url": video_url,
        }
        response = requests.post(url, headers=headers, json=data)
        if response.status_code == 201:
            return {"success": "Message sent successfully!", "data": response.json()}
        else:
            return {"error": response.text}
    except Exception as error:
        return {"error": str(error)}
