#-----------------------------------------------------
# Main entry for storage service API.
#
# Receives processed trend snapshots from processing and stores them in
# PostgreSQL. Also serves latest trend data to the dashboard.
#
#   -- Open Design --
#   Processing and dashboard talk to this API instead of connecting to the
#   database directly.
#
#   -- Security --
#   Database credentials stay in the storage service scope.
#
#   -- Transparency --
#   API endpoints make reads and writes visible in storage service logs.
#
#   -- Availability --
#   Dashboard can keep reading latest saved snapshots even if ingestion or
#   processing temporarily stops.
#-----------------------------------------------------

from flask import Flask, jsonify, request

from services.logging_utils import get_logger
from services.storage.database_store import DatabaseTrendStore


logger = get_logger("services.storage.main")

app = Flask(__name__)
store = DatabaseTrendStore()


# allow dashboard running from a different port to call this API
@app.after_request
def add_cors_headers(response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type"
    response.headers["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS"
    return response


# dashboard reads latest trend counts from this endpoint
@app.get("/api/latest-trends")
def latest_trends():
    return jsonify(store.latest_trends() or [])


# dashboard reads latest example posts from this endpoint
@app.get("/api/latest-examples")
def latest_examples():
    return jsonify(store.latest_examples() or [])


# processing sends trend counts here after each snapshot interval
@app.post("/api/trend-snapshots")
def save_trend_snapshot():
    payload = request.get_json(silent=True) or {}
    trends = [
        (item.get("term"), item.get("count"))
        for item in payload.get("trends", [])
    ]

    store.save_snapshot(payload.get("posts_processed", 0), trends)
    logger.info("Stored trend snapshot from API request.")
    return jsonify({"status": "ok"}), 201


# processing sends example posts here after each snapshot interval
@app.post("/api/example-posts")
def save_example_posts():
    payload = request.get_json(silent=True) or {}

    store.save_example_posts(
        payload.get("posts_processed", 0),
        payload.get("examples", []),
    )
    logger.info("Stored example posts from API request.")
    return jsonify({"status": "ok"}), 201


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
