import os
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

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
    description = f"""{script_text[:400]}...

🔔 Subscribe for daily manga reviews!
#manga #anime #{manga_info['manga_title'].replace(' ', '')}
"""

    body = {
        "snippet": {
            "title": title,
            "description": description,
            "tags": ["manga", "anime", manga_info["manga_title"], "chapter review"],
            "categoryId": "24"
        },
        "status": {
            "privacyStatus": "public"
        }
    }

    media = MediaFileUpload(video_path, mimetype="video/mp4", resumable=True)

    request = youtube.videos().insert(
        part="snippet,status",
        body=body,
        media_body=media
    )

    response = request.execute()
    print(f"Video uploaded! ID: {response['id']}")
    return response["id"]
