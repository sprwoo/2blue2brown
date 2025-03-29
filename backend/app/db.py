import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

SUPABASE_URL = os.getenv('supaurl')
SUPABASE_ANON_KEY = os.getenv('supakey')

"""
    To connect to a database, the url should be:
        url = f"{SUPABASE_URL}/rest/v1/{table_name}?"

    and the header:
        headers = {
            'Content-Type': ...,
            'Accept': ...,
            'apikey': SUPABASE_ANON_KEY,
            'Authorization': f'Bearer {SUPABASE_ANON_KEY}',
            'Accept-Profile': 'chatbotschema' # IF DOING A GET REQUEST
            'Content-Profile': 'chatbotschema' # IF DOING A POST REQUEST
        }

    Then you should be able to make GET or POST requests to the database.
"""

def check_connection():
    try:
        # Use the correct endpoint for the table (schema name should not be in the path)
        url = f"{SUPABASE_URL}/rest/v1/chat_messages?"
        
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'apikey': SUPABASE_ANON_KEY,
            'Authorization': f'Bearer {SUPABASE_ANON_KEY}',
            'Accept-Profile': 'chatbotschema'
        }
        
        response = requests.get(url, headers=headers)
        print(f"Response Status: {response.status_code}")
        
        if response.status_code == 200:
            print("Database connection successful!")
            print("Response Body:", response.json())
        else:
            print("Error connecting to database:", response.text)
    
    except Exception as error:
        print("An error occurred:", error)

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
        print(f"Response Status: {response.status_code}")
        
        if response.status_code == 201:
            print("Data posted successfully!")
            print("Response Body:", response.json())
        else:
            print("Error posting data:", response.text)
    
    except Exception as error:
        print("An error occurred:", error)

if __name__ == '__main__':
    post_test()
