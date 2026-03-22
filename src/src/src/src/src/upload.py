import os
import google.auth
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google.oauth2.credentials import Credentials

def upload_video(video_path, manga_info, script_text):
    creds = Credentials(
        token=None,
        refresh_token=os.environ["YOUTUBE_REFRESH_TOKEN"],
        client_id=os.environ["YOUTUBE_CLIENT_ID"],
        client_secret=os.environ["YOUTUBE_CLIENT_SECRET"],
        token_uri="https://oauth2.googleapis.com/token"
    )

    youtube = build("youtube", "v3", credentials=creds)

    title = f"{manga_info['manga_title']} Chapter {manga_info['chapter']} Review!"
    description = f"""
{script_text[:400]}...

🔔 Subscribe for daily manga reviews!
#manga #anime #{manga_info['manga_title'].replace(' ','')}
"""

    body = {
        "snippet": {
            "title": title,
            "description": description,
            "tags": ["manga", "a
