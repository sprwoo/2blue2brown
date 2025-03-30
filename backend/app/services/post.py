import requests

url = "http://127.0.0.1:5001/api/post_chat_session"
headers = {
    "Content-Type": "application/json"
}
data = {
    "session_title": "Test Chat Session"
}

response = requests.post(url, headers=headers, json=data)

if response.status_code == 200:
    print("Response:", response.json())
else:
    print("Error:", response.status_code, response.text)