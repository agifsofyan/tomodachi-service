FROM python:3.14-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY --from=ghcr.io/astral-sh/uv:0.5.11 /uv /uvx /bin/

COPY pyproject.toml uv.lock ./
RUN uv sync --frozen --no-dev

# Buat user
RUN groupadd -r appuser && useradd -r -g appuser appuser

COPY --chown=appuser:appuser . .

RUN chmod +x /app/deployment/start.sh

ENV PATH="/app/.venv/bin:$PATH"

USER appuser

EXPOSE 8000

CMD ["./deployment/start.sh"]