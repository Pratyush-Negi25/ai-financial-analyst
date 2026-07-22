"""
AI Financial Analyst API — FastAPI application entry point.

Initializes configuration, logging, CORS, and API routers.
Swagger UI is available at /docs (enabled by default in development).
"""

from contextlib import asynccontextmanager
from collections.abc import AsyncIterator

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.router import api_router
from app.core.config import get_settings
from app.core.logging import get_logger, setup_logging

logger = get_logger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator[None]:
    """Application startup and shutdown lifecycle hooks."""
    settings = get_settings()
    setup_logging(settings)
    logger.info("Starting %s v%s [%s]", settings.app_name, settings.app_version, settings.app_env)
    yield
    logger.info("Shutting down %s", settings.app_name)


def create_app() -> FastAPI:
    """Create and configure the FastAPI application."""
    settings = get_settings()

    app = FastAPI(
        title=settings.app_name,
        version=settings.app_version,
        description=(
            "Production API for the AI Financial Analyst — upload financial documents "
            "and chat with them using Retrieval-Augmented Generation (RAG)."
        ),
        docs_url="/docs" if settings.debug else "/docs",
        redoc_url="/redoc" if settings.debug else "/redoc",
        openapi_url="/openapi.json",
        lifespan=lifespan,
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.cors_origin_list,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(api_router)

    return app


app = create_app()
