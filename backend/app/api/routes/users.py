from typing import Any

from app.api.deps import SessionDepends
from app.core.config import settings
from app.schemas import UserCreate, UserRead, UserTelegramData
from fastapi import APIRouter, Depends, HTTPException

router = APIRouter()
