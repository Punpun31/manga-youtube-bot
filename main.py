import random
import os
from discover import get_new_chapters
from script import generate_script
from voiceover import generate_voiceover
from render import render_video
from upload import upload_video

def run():
    print("Fetching new manga chapters...")
    chapters = get_new_chapters(limit=1)

    if not chapters:
        print("No new chapters found today.")
        return

    manga = random.choice(chapters)
    print(f"Selected: {manga['manga_title']} - Chapter {manga['chapter']}")

    print("Generating script...")
    script = generate_script(manga)

    print("Generating voiceover...")
    voiceover_path = generate_voiceover(script)

    print("Rendering video...")
    video_path = render_video(manga, voiceover_path)

    print("Uploading to YouTube...")
    upload_video(video_path, manga, script)

    print("Done! Video published successfully.")

if __name__ == "__main__":
    run()
