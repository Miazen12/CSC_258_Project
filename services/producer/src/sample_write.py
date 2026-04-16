import json
from src.config import SAVE_SAMPLE_PATH


class SampleWriter:
    def __init__(self, max_posts=100):
        self.max_posts = max_posts
        self.posts = []

    def add_post(self, post: dict):
        self.posts.append(post)
        print(f"Captured {len(self.posts)} posts")

    def is_full(self):
        return len(self.posts) >= self.max_posts

    def save(self):
        with open(SAVE_SAMPLE_PATH, "w", encoding="utf-8") as f:
            json.dump(self.posts, f, indent=2, ensure_ascii=False)
        print(f"Saved {len(self.posts)} posts to {SAVE_SAMPLE_PATH}")