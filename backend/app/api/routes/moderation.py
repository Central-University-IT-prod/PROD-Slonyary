from typing import Annotated

from fastapi import APIRouter, Depends
from starlette import status

from app.api.depends.moderation import accept_post_dep, downgrade_post_dep
from app.schemas import Result
from shared.database.models import Post

router = APIRouter(prefix="/posts/{post_id}", tags=["moderation"])


@router.post("/accept", status_code=status.HTTP_200_OK)
async def accept_post(_: Annotated[Post, Depends(accept_post_dep)]) -> Result:
    return Result(status="ok")


@router.post("/downgrade", status_code=status.HTTP_200_OK)
async def downgrade_post(_: Annotated[Post, Depends(downgrade_post_dep)]) -> Result:
    return Result(status="ok")
