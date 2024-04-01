from app.api.deps import CurrentUserDep, SessionDepends
from app.schemas import PreviewPost, TgChannelRead
from fastapi import APIRouter

router = APIRouter()


@router.get("/", status_code=200)
async def get_posts(user: CurrentUserDep, db: SessionDepends) -> list[PreviewPost]:
    pass

@router.post("/create", status_code=200)
async def create_post(user: CurrentUserDep):
    pass

@router.get("/{id}", status_code=200)
async def get_post(
    user: CurrentUserDep, db: SessionDepends, id: int
) -> list[TgChannelRead]:
    pass
