import unittest

from services.processing.processor import TrendProcessor


class TrendProcessorTests(unittest.TestCase):
    def setUp(self):
        self.processor = TrendProcessor()

    def test_process_post_counts_terms_and_phrases(self):
        post = {
            "post_id": "post-1",
            "timestamp": "2026-05-03T12:00:00Z",
            "text": "OpenAI builds #Testing systems",
            "author": "did:plc:author1",
            "source": "bluesky",
            "is_repost": False,
        }

        processed = self.processor.process_post(post)

        self.assertTrue(processed)
        self.assertEqual(self.processor.posts_processed, 1)
        self.assertIn("#testing", self.processor.topic_counts)
        self.assertIn("openai", self.processor.topic_counts)
        self.assertIn("builds", self.processor.topic_counts)
        self.assertIn("systems", self.processor.topic_counts)
        self.assertIn("openai builds", self.processor.topic_counts)

    def test_process_post_rejects_invalid_payload(self):
        invalid_post = {
            "post_id": "",
            "timestamp": "2026-05-03T12:00:00Z",
            "text": "Hello world",
            "author": "did:plc:author1",
            "source": "bluesky",
            "is_repost": False,
        }

        processed = self.processor.process_post(invalid_post)

        self.assertFalse(processed)
        self.assertEqual(self.processor.invalid_posts_skipped, 1)
        self.assertEqual(self.processor.posts_processed, 0)


if __name__ == "__main__":
    unittest.main()
