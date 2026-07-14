#!/bin/sh
set -e

echo "===== START.SH EXECUTED ====="

pwd
ls -la
ls -la app

echo "Running migrations..."
alembic upgrade head

echo "Testing import..."
python -c "from app.main import app; print(app)"

echo "Starting FastAPI..."

exec uv run uvicorn app.main:app \
    --host 0.0.0.0 \
    --port ${PORT:-8000}