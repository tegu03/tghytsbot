# tghytsbot/upload_to_youtube.py

import os
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import pickle

SCOPES = ["https://www.googleapis.com/auth/youtube.upload"]

def get_authenticated_service():
    creds = None
    if os.path.exists("credentials/token.pickle"):
        with open("credentials/token.pickle", "rb") as token:
            creds = pickle.load(token)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                "credentials/client_secret.json", SCOPES)
            creds = flow.run_local_server(port=0)

        with open("credentials/token.pickle", "wb") as token:
            pickle.dump(creds, token)

    return build("youtube", "v3", credentials=creds)

def upload_video(video_file, title="My Shorts", description="", tags=None, privacy="public"):
    youtube = get_authenticated_service()

    body = {
        "snippet": {
            "title": title,
            "description": description,
            "tags": tags or ["AI", "Short", "funny"],
            "categoryId": "22"
        },
        "status": {
            "privacyStatus": privacy
        }
    }

    media_file = MediaFileUpload(video_file, chunksize=-1, resumable=True, mimetype="video/*")
    request = youtube.videos().insert(part="snippet,status", body=body, media_body=media_file)
    response = request.execute()
    print(f"✅ Video berhasil diupload: https://www.youtube.com/watch?v={response['id']}")

if __name__ == "__main__":
    upload_video("output/final_video.mp4", title="Short by AI Bot #upinipin #dontol")
