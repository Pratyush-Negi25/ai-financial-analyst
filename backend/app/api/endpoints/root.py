"""Root API endpoints."""

from fastapi import APIRouter, Depends, status

from app.api.dependencies import get_health_service
from app.models.health import RootResponse
from app.services.health_service import HealthService

router = APIRouter(tags=["Root"])


@router.get(
    "/",
    response_model=RootResponse,
    status_code=status.HTTP_200_OK,
    summary="API root",
    description="Returns basic API information and useful links.",
)
def read_root(
    health_service: HealthService = Depends(get_health_service),
) -> RootResponse:
    """Return API welcome message and navigation links."""
    return health_service.get_root()
