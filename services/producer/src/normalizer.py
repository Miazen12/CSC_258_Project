from src.config import SOURCE_NAME


def normalize_post(event: dict):

    commit = event.get("commit", {})
    record = commit.get("record", {})

    text = record.get("text")
    created_at = record.get("createdAt")
    did = event.get("did")
    rkey = commit.get("rkey")

    if not text:
        return None

    post_id = f"{did}:{rkey}" if did and rkey else did or "unknown"

    return {
        "post_id": post_id,
        "timestamp": created_at,
        "text": text,
        "author": did,
        "source": SOURCE_NAME,
        "is_repost": False,
    }