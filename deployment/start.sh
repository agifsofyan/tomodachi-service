#!/bin/sh

set -e

echo "Starting FastAPI..."

exec uvicorn app.main:app \
    --host 0.0.0.0 \
    --port "${PORT:-8000}"