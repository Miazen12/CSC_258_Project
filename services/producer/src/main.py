from bluesky_consumer import BlueskyConsumer
from normalizer import normalize_post
from sample_write import SampleWriter
from config import MAX_SAMPLE_POSTS

writer = SampleWriter(max_posts=MAX_SAMPLE_POSTS)

def handle_event(event, ws):
    post = normalize_post(event)
    if not post:
        return

    writer.add_post(post)

    if writer.is_full():
        writer.save()
        ws.stop_requested = True
        ws.close()

if __name__ == "__main__":
    consumer = BlueskyConsumer(on_event=handle_event)
    consumer.run()