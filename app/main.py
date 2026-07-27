"""FastAPI Application Entry Point"""

import logging
import sys

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.v1.api import api_router
from app.core.config import settings
from app.core.exceptions.handlers import register_exception_handlers

logging.basicConfig(
    level=logging.INFO,
    stream=sys.stdout,
    force=True,  # Python >=3.8
)

app = FastAPI(
    title=settings.PROJECT_NAME
    if hasattr(settings, "PROJECT_NAME")
    else "FastAPI Application",
    version="1.0.0",
    description="Clean Architecture FastAPI Application",
)

register_exception_handlers(app)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router)


@app.get("/health")
def health_check():
    return {"status": "healthy"}
