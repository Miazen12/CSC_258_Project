# Producer Service

This service connects to Bluesky Jetstream, filters for post records, normalizes them,
and saves a sample dataset for downstream processing.

## Files

- `src/config.py` - connection settings
- `src/bluesky_consumer.py` - WebSocket listener
- `src/normalizer.py` - maps Bluesky events to internal schema
- `src/sample_write.py` - saves normalized posts
- `src/main.py` - entry point

## Run locally

```bash
pip install -r requirements.txt
python src/main.py
```
