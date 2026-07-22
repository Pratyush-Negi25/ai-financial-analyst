"""Health check API endpoints."""

from fastapi import APIRouter, Depends, status

from app.api.dependencies import get_health_service
from app.models.health import HealthResponse
from app.services.health_service import HealthService

router = APIRouter(tags=["Health"])


@router.get(
    "/health",
    response_model=HealthResponse,
    status_code=status.HTTP_200_OK,
    summary="Health check",
    description="Returns the current health status of the API.",
)
def health_check(
    health_service: HealthService = Depends(get_health_service),
) -> HealthResponse:
    """Verify that the API is running and responsive."""
    return health_service.get_health()
