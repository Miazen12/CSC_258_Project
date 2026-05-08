#-----------------------------------------------------
# Storage service config.
#
#   -- Open Design --
#   SQL file paths and service URLs are kept here so the storage logic can
#   change without hardcoding paths in multiple files.
#
#   -- Scalability --
#   Database storage replaces growing JSON files with PostgreSQL tables.
#
#   -- Security --
#   DATABASE_URL should come from environment variables in Docker/cloud.
#
#   -- Transparency --
#   Keeping the SQL files under sql_lib makes database operations easier to see.
#-----------------------------------------------------

import os

# old JSON paths kept for the original local file store
TREND_SNAPSHOT_PATH = "services/storage/logs/trends.json"
TREND_EXAMPLE_POSTS_PATH = "services/storage/logs/example_posts.json"


# DDL and SQL query files used by DatabaseTrendStore
CREATE_TABLE_SQL_PATH = "services/storage/sql_lib/create_tables.sql"
INSERT_TREND_SNAPSHOT_SQL_PATH = "services/storage/sql_lib/insert_trend_snapshot.sql"
INSERT_TREND_TERM_SQL_PATH = "services/storage/sql_lib/insert_trend_term.sql"
INSERT_TREND_EXAMPLE_SQL_PATH = "services/storage/sql_lib/insert_trend_example.sql"
SELECT_LATEST_TRENDS_SQL_PATH = "services/storage/sql_lib/select_latest_trends.sql"
SELECT_LATEST_EXAMPLES_SQL_PATH = "services/storage/sql_lib/select_latest_examples.sql"

# database connection for the storage service
DATABASE_URL = os.getenv("DATABASE_URL","postgresql://trend_user:trend_password@localhost:5432/trends_db")

# API URL used by processing when it sends snapshots to storage
STORAGE_API_URL = os.getenv("STORAGE_API_URL", "http://localhost:5001")
