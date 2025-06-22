# upload_to_youtube.py

import os
import sys
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import pickle

from config import OUTPUT_VIDEO

# YouTube API scope
SCOPES = ["https://www.googleapis.com/auth/youtube.upload"]
CREDENTIALS_FILE = "credentials/client_secret.json"
TOKEN_FILE = "credentials/token.pickle"

def get_authenticated_service():
    creds = None
    if os.path.exists(TOKEN_FILE):
        with open(TOKEN_FILE, "rb") as token:
            creds = pickle.load(token)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                CREDENTIALS_FILE, SCOPES
            )
            creds = flow.run_local_server(port=0)

        os.makedirs("credentials", exist_ok=True)
        with open(TOKEN_FILE, "wb") as token:
            pickle.dump(creds, token)

    return build("youtube", "v3", credentials=creds)

def upload_video(video_file, title="Short Video by Bot", description="", tags=None):
    youtube = get_authenticated_service()

    print("📤 Mengunggah video ke YouTube...")

    body = {
        "snippet": {
            "title": title,
            "description": description,
            "tags": tags or ["short", "funny", "upinipin"],
            "categoryId": "22"
        },
        "status": {
            "privacyStatus": "public",
            "selfDeclaredMadeForKids": False,
        }
    }

    if not os.path.exists(video_file):
        print(f"❌ File video tidak ditemukan: {video_file}")
        return

    media_file = MediaFileUpload(video_file, chunksize=-1, resumable=True, mimetype="video/mp4")
    request = youtube.videos().insert(part="snippet,status", body=body, media_body=media_file)
    response = None
    while response is None:
        status, response = request.next_chunk()
        if status:
            print(f"⬆️ Upload {int(status.progress() * 100)}%")

    print(f"✅ Video berhasil diunggah! Video ID: {response['id']}")

if __name__ == "__main__":
    upload_video(OUTPUT_VIDEO, title="Short by AI Bot #upinipin #dontol")
