"""Response schemas for health and status endpoints."""

from pydantic import BaseModel, Field


class HealthResponse(BaseModel):
    """Health check response payload."""

    status: str = Field(..., examples=["healthy"])
    app_name: str = Field(..., examples=["AI Financial Analyst API"])
    version: str = Field(..., examples=["1.0.0"])
    environment: str = Field(..., examples=["development"])


class RootResponse(BaseModel):
    """Root endpoint response payload."""

    message: str = Field(..., examples=["AI Financial Analyst API is running!"])
    docs_url: str = Field(..., examples=["/docs"])
    health_url: str = Field(..., examples=["/health"])
