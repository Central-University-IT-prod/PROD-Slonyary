from typing import Annotated

from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from app.core.db import get_db_session
from app.models import User

SessionDepends = Annotated[Session, Depends(get_db_session)]

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


async def get_current_user(
    db: SessionDepends,
    token: Annotated[str, Depends(oauth2_scheme)],
) -> User:
    pass


CurrentUserDep = Annotated[User, Depends(get_current_user)]
