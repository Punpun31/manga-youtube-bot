import google.generativeai as genai
import os

def generate_script(manga_info):
    genai.configure(api_key=os.environ["GEMINI_API_KEY"])
    model = genai.GenerativeModel("gemini-2.0-flash")

    prompt = f"""
You are an enthusiastic manga YouTuber. Write an engaging YouTube video script for the following manga chapter:

Manga: {manga_info['manga_title']}
Chapter: {manga_info['chapter']}
Volume: {manga_info['volume']}
Pages: {manga_info['pages']}

The script should:
- Start with a strong hook (first 15 seconds)
- Give a brief overview of the manga for new viewers
- Review and discuss this specific chapter excitedly
- End with a call to action (like, subscribe, comment)
- Be around 600-800 words
- Sound natural and conversational, not robotic

Write only the script text, no stage directions or labels.
"""

    response = model.generate_content(prompt)
    return response.text
