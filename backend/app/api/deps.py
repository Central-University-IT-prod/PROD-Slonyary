from typing import Annotated

from app.core import security
from app.core.config import settings
from app.core.db import SessionLocal, engine
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from pydantic import ValidationError
from sqlalchemy.orm import Session

reusable_oauth2 = OAuth2PasswordBearer(
    tokenUrl=f"{settings.API_V1_STR}/login/access-token"
)


async def get_db():
    async with SessionLocal() as session:
        yield session


SessionDep = Annotated[Session, Depends(get_db)]
