from typing import Any

from app.api.deps import SessionDep
from app.core.config import settings
from app.core.security import get_password_hash, verify_password
from app.utils import generate_new_account_email, send_email
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import col, delete, func, select

router = APIRouter()
