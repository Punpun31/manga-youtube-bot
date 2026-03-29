import requests
from datetime import datetime, timedelta
import random

def get_new_chapters(limit=10):
    yesterday = (datetime.utcnow() - timedelta(days=1)).strftime("%Y-%m-%dT%H:%M:%S")
    
    url = "https://api.mangadex.org/chapter"
    params = {
        "translatedLanguage[]": "en",
        "publishAtSince": yesterday,
        "order[publishAt]": "desc",
        "limit": limit,
        "includes[]": "manga"
    }
    
    response = requests.get(url, params=params)
    data = response.json()
    
    results = []
    for chapter in data["data"]:
        manga_title = "Unknown"
        for rel in chapter["relationships"]:
            if rel["type"] == "manga":
                attrs = rel.get("attributes", {})
                titles = attrs.get("title", {})
                manga_title = titles.get("en") or list(titles.values())[0] if titles else "Unknown"
        
        results.append({
            "manga_title": manga_title,
            "chapter": chapter["attributes"].get("chapter", "?"),
            "volume": chapter["attributes"].get("volume", "?"),
            "pages": chapter["attributes"].get("pages", 0),
        })
    
    random.shuffle(results)
    return results

if __name__ == "__main__":
    chapters = get_new_chapters()
    for c in chapters:
        print(f"{c['manga_title']} — Chapter {c['chapter']}")
