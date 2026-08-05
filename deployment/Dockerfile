FROM python:3.14-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Install uv
COPY --from=ghcr.io/astral-sh/uv:0.5.11 /uv /uvx /bin/

# Copy dependency file
COPY pyproject.toml uv.lock ./

# Install dependencies ke .venv
RUN uv sync --frozen --no-dev

# Copy source code
COPY . .

# Buat user non-root
RUN groupadd -r appuser && \
    useradd -r -m -d /home/appuser -g appuser appuser

# Permission
RUN chmod +x /app/deployment/start.sh && \
    chown -R appuser:appuser /app /home/appuser

# Gunakan virtualenv
ENV PATH="/app/.venv/bin:$PATH"

USER appuser

EXPOSE 8000

CMD ["/app/deployment/start.sh"]