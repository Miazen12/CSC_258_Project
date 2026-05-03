import os


KAFKA_BOOTSTRAP_SERVERS = os.getenv("KAFKA_BOOTSTRAP_SERVERS", "localhost:9092")
SOCIAL_POSTS_TOPIC = os.getenv("SOCIAL_POSTS_TOPIC", "BlueSky_socialmedia_posts")
