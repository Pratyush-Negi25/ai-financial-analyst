"""Business logic for health and status checks."""

from app.core.config import Settings
from app.models.health import HealthResponse, RootResponse


class HealthService:
    """Service layer for application health and status operations."""

    def __init__(self, settings: Settings) -> None:
        self._settings = settings

    def get_health(self) -> HealthResponse:
        """Return current application health status."""
        return HealthResponse(
            status="healthy",
            app_name=self._settings.app_name,
            version=self._settings.app_version,
            environment=self._settings.app_env,
        )

    def get_root(self) -> RootResponse:
        """Return root endpoint metadata."""
        return RootResponse(
            message=f"{self._settings.app_name} is running!",
            docs_url="/docs",
            health_url="/health",
        )
