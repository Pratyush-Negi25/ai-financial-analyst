"""Main API router aggregating all endpoint modules."""

from fastapi import APIRouter

from app.api.endpoints import chat, health, root, upload

api_router = APIRouter()

api_router.include_router(root.router)
api_router.include_router(health.router)
api_router.include_router(upload.router)
api_router.include_router(chat.router)