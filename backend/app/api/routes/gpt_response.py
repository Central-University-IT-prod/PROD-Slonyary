from fastapi import APIRouter

router = APIRouter(prefix="/gpt_response")


@router.get("", status_code=200)
async def get_gpt_response(prompt: str):
    return "ok"
