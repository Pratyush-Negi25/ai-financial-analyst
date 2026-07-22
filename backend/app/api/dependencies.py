"""FastAPI dependency injection providers."""

from functools import lru_cache

from app.core.config import Settings, get_settings
from app.services.health_service import HealthService


@lru_cache
def get_health_service() -> HealthService:
    """Provide a cached HealthService instance."""
    return HealthService(settings=get_settings())


def get_app_settings() -> Settings:
    """Provide application settings via dependency injection."""
    return get_settings()
