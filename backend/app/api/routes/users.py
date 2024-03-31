from typing import Any

from app.api.deps import SessionDep
from app.core.config import settings
from app.schemas import UserCreate, UserOut, UserTelegramData
from fastapi import APIRouter, Depends, HTTPException

router = APIRouter()
