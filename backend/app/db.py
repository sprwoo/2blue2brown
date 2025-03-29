import os
import requests
from dotenv import load_dotenv

load_dotenv()

SUPABASE_URL = os.getenv('supaurl')
SUPABASE_ANON_KEY = os.getenv('supakey')

def check_connection():
    try:
        url = f"{SUPABASE_URL}/rest/v1/Papers?limit=1"
        headers = {
            'Content-Type': 'application/json',
            'apikey': SUPABASE_ANON_KEY,
            'Authorization': f'Bearer {SUPABASE_ANON_KEY}'
        }
        response = requests.get(url, headers=headers)
        print("Response Status:", response.status_code)
        
        if response.status_code == 200:
            print("Database connection successful!")
            result = response.json()
            print("Response Body:", result)
        else:
            print("Error connecting to database:", response.text)
    except Exception as error:
        print("An error occurred:", error)

if __name__ == '__main__':
    check_connection()
