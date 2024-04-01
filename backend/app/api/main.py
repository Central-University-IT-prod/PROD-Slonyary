from fastapi import APIRouter

from app.api.routes import auth, channel, ping, post

api_router = APIRouter()
api_router.include_router(auth.router, prefix="/auth", tags=["auth"])
api_router.include_router(post.router, prefix="/posts", tags=["post"])
api_router.include_router(channel.router, prefix="/channels", tags=["channel"])
api_router.include_router(ping.router, tags=["ping"])
