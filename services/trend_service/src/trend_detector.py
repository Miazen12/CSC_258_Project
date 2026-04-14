import json
import time
import re
from collections import Counter, deque
from pathlib import Path

WINDOW_SIZE = 10

BASE_DIR = Path(__file__).resolve().parents[3]
FILE_PATH = BASE_DIR / "storage" / "data" / "sample_post.json"

window = deque(maxlen=WINDOW_SIZE)

def clean_text(text: str) -> str:
    text = text.lower()
    text = re.sub(r"[^\w\s#]", "", text)
    return text

def extract_keywords(text: str) -> list[str]:
    words = text.split()
    return [w.replace("#", "") for w in words if w.startswith("#")]

def load_posts() -> list:
    try:
        with open(FILE_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        print(f"Error loading posts: {e}")
        return []

print("Trend Service Started...\n")

while True:
    posts = load_posts()

    if not posts:
        print("No data found yet...")
        time.sleep(3)
        continue

    window.clear()

    for post in posts[-WINDOW_SIZE:]:
        text = clean_text(post.get("text", ""))
        keywords = extract_keywords(text)
        window.append(keywords)

    all_keywords = [word for sublist in window for word in sublist]
    counter = Counter(all_keywords)

    print("\nCurrent Trends:")
    if counter:
        for word, count in counter.most_common(5):
            print(f"{word}: {count}")
    else:
        print("No hashtags found in current posts.")

    print("-" * 40)
    time.sleep(5)