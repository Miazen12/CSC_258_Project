import json
import websocket
from config import JETSTREAM_URL


class BlueskyConsumer:
    def __init__(self, on_event):
        self.on_event = on_event

    def _on_open(self, ws):
        print("Connected to Bluesky Jetstream")

    def _on_message(self, ws, message):
        try:
            event = json.loads(message)
        except json.JSONDecodeError:
            return

        self.on_event(event, ws)

    def _on_error(self, ws, error):
        print("WebSocket error:", error)

    def _on_close(self, ws, close_status_code, close_msg):
        print("Connection closed:", close_status_code, close_msg)

    def run(self):
        ws = websocket.WebSocketApp(
            JETSTREAM_URL,
            on_open=self._on_open,
            on_message=self._on_message,
            on_error=self._on_error,
            on_close=self._on_close,
        )
        ws.run_forever()