from fastapi import APIRouter

router = APIRouter()


@router.get("/ping", status_code=200)
async def ping():
    return "ok"
