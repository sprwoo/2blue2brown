import os
from dotenv import load_dotenv
import requests
import mimetypes

# Load environment variables from the .env file
load_dotenv()

# Supabase configuration from environment variables
SUPABASE_URL = os.getenv("supaurl")
SUPABASE_KEY = os.getenv("supakey")
BUCKET_NAME = "images"  # Replace with your actual bucket name

# File details
file_path = "dawg.jpg"     # Adjust to your file path
file_name = "myimasge.jpg"  # Desired name in storage

# Determine the MIME type of the file
mime_type, _ = mimetypes.guess_type(file_path)
if mime_type is None:
    mime_type = "application/octet-stream"  # Fallback MIME type
print("Detected MIME type:", mime_type)

# Construct the upload URL including the 'upsert' query parameter
upload_url = f"{SUPABASE_URL}/storage/v1/object/{BUCKET_NAME}/{file_name}?upsert=true"

# Read the file in binary mode
with open(file_path, "rb") as file:
    file_data = file.read()

# Define the upload headers
headers = {
    "Authorization": f"Bearer {SUPABASE_KEY}",
    "Content-Type": mime_type,
}

# Make the PUT request to upload the file
response = requests.put(upload_url, headers=headers, data=file_data)

# Check the response and print the result
if response.status_code == 200:
    print("✅ Upload successful!")
    print(f"📂 File URL: {SUPABASE_URL}/storage/v1/object/public/{BUCKET_NAME}/{file_name}")
else:
    print("❌ Upload failed:", response.text)
