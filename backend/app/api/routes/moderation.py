from typing import Annotated

from app.api.depends.moderation import (
    accept_post_dep,
    downgrade_post_dep,
    reject_post_dep,
)
from app.schemas import Result
from fastapi import APIRouter, Depends
from shared.database.models import Post
from starlette import status

router = APIRouter(prefix="/posts/{post_id}", tags=["moderation"])


@router.post("/accept", status_code=status.HTTP_200_OK)
async def accept_post(_: Annotated[Post, Depends(accept_post_dep)]) -> Result:
    return Result(status="ok")


@router.post("/downgrade", status_code=status.HTTP_200_OK)
async def downgrade_post(_: Annotated[Post, Depends(downgrade_post_dep)]) -> Result:
    return Result(status="ok")


@router.delete("/reject", status_code=200)
async def reject_post(_: Annotated[Post, Depends(reject_post_dep)]) -> Result:
    return Result(status="ok")
