import os
from pathlib import Path


def find_base_dir() -> Path:
    current_file = Path(__file__).resolve()

    for parent in current_file.parents:
        if (parent / "services").exists() or (parent / "storage").exists():
            return parent

    return current_file.parents[1]


BASE_DIR = Path(os.getenv("PROJECT_ROOT", find_base_dir()))

JETSTREAM_URL = (
    "wss://jetstream1.us-east.bsky.network/subscribe"
    "?wantedCollections=app.bsky.feed.post"
)

SOURCE_NAME = "bluesky"
SAVE_SAMPLE_PATH = Path(
    os.getenv(
        "SAVE_SAMPLE_PATH",
        str(BASE_DIR / "storage" / "data" / "sample_post.json"),
    )
)
MAX_SAMPLE_POSTS = 10000
