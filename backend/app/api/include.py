from fastapi import APIRouter

from app.api.routes import auth, channels, links, moderation, ping, posts

api_router = APIRouter()

for router in (
    auth.router,
    posts.router,
    channels.router,
    ping.router,
    links.router,
    moderation.router,
):
    api_router.include_router(router)
