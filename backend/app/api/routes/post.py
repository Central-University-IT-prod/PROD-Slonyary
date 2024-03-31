from fastapi import APIRouter

from app.api.deps import CurrentUserDep, SessionDep
from app.schemas import PreviewPost, TgChannelOut

router = APIRouter()


@router.get("/", status_code=200)
async def get_posts(user: CurrentUserDep, db: SessionDep) -> list[PreviewPost]:
    pass


@router.get("/{id}", status_code=200)
async def get_post(user: CurrentUserDep, db: SessionDep, id: int) -> list[TgChannelOut]:
    pass
