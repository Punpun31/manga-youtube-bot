import os
import requests

def generate_script(manga_info):
    api_key = os.environ["GROQ_API_KEY"]
    
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    prompt = f"""You are an enthusiastic manga YouTuber. Write an engaging YouTube video script for the following manga chapter:

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

Write only the script text, no stage directions or labels."""

    data = {
        "model": "llama-3.3-70b-versatile",
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": 1500
    }
    
    response = requests.post(
        "https://api.groq.com/openai/v1/chat/completions",
        headers=headers,
        json=data
    )
    
    return response.json()["choices"][0]["message"]["content"]
