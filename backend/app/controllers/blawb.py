import os
from dotenv import load_dotenv
import requests
import mimetypes

load_dotenv()

class SupabaseStorage:
    def __init__(self):
        self.supabase_url = os.getenv("supaurl")
        self.supabase_key = os.getenv("supakey")
        self.bucket_name = "images"

    def upload_file(self, file_path, file_name=None):
        if file_name is None:
            file_name = os.path.basename(file_path)
        mime_type, _ = mimetypes.guess_type(file_path)
        if mime_type is None:
            if file_path.lower().endswith(".mp4"):
                mime_type = "video/mp4"
            else:
                mime_type = "application/octet-stream"
        upload_url = f"{self.supabase_url}/storage/v1/object/{self.bucket_name}/{file_name}?upsert=true"
        with open(file_path, "rb") as file:
            file_data = file.read()
        headers = {
            "Authorization": f"Bearer {self.supabase_key}",
            "Content-Type": mime_type,
        }
        response = requests.put(upload_url, headers=headers, data=file_data)
        if response.status_code == 200:
            return f"{self.supabase_url}/storage/v1/object/public/{self.bucket_name}/{file_name}"
        else:
            raise Exception("Upload failed: " + response.text)

    def retrieve_file(self, file_name, download_path=None):
        url = f"{self.supabase_url}/storage/v1/object/public/{self.bucket_name}/{file_name}"
        response = requests.get(url)
        if response.status_code == 200:
            if download_path:
                with open(download_path, "wb") as f:
                    f.write(response.content)
            return response.content
        else:
            raise Exception("Retrieve failed: " + response.text)