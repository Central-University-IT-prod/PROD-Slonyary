from app.api.routes import auth, channel, post
from fastapi import APIRouter

api_router = APIRouter()
api_router.include_router(auth.router, prefix="/auth", tags=["auth"])
api_router.include_router(post.router, prefix="/posts", tags=["post"])
api_router.include_router(post.router, prefix="/channels", tags=["channel"])
