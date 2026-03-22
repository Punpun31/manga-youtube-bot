import subprocess
import os
import requests

def download_thumbnail(manga_title, output_path="output/thumbnail.jpg"):
    os.makedirs("output", exist_ok=True)
    url = f"https://api.mangadex.org/manga"
    params = {"title": manga_title, "limit": 1, "includes[]": "cover_art"}
    response = requests.get(url, params=params)
    data = response.json()

    try:
        manga_id = data["data"][0]["id"]
        cover = next(r for r in data["data"][0]["relationships"] if r["type"] == "cover_art")
        filename = cover["attributes"]["fileName"]
        img_url = f"https://uploads.mangadex.org/covers/{manga_id}/{filename}.256.jpg"
        img_data = requests.get(img_url).content
        with open(output_path, "wb") as f:
            f.write(img_data)
    except Exception:
        open(output_path, "wb").close()

    return output_path

def render_video(manga_info, voiceover_path, output_path="output/final_video.mp4"):
    os.makedirs("output", exist_ok=True)
    thumbnail = download_thumbnail(manga_info["manga_title"])
    title_text = f"{manga_info['manga_title']} - Chapter {manga_info['chapter']}"

    subprocess.run([
        "ffmpeg", "-y",
        "-loop", "1",
        "-i", thumbnail,
        "-i", voiceover_path,
        "-vf", f"scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2,drawtext=text='{title_text}':fontsize=60:fontcolor=white:x=(w-text_w)/2:y=h-120:box=1:boxcolor=black@0.5:boxborderw=10",
        "-c:v", "libx264",
        "-tune", "stillimage",
        "-c:a", "aac",
        "-b:a", "192k",
        "-pix_fmt", "yuv420p",
        "-shortest",
        output_path
    ], check=True)

    return output_path

if __name__ == "__main__":
    test = {
        "manga_title": "One Piece",
        "chapter": "1100",
        "volume": "110",
        "pages": "17"
    }
    render_video(test, "output/voiceover.wav")
    print("Video rendered!")
