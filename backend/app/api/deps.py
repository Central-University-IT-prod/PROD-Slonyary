from typing import Annotated

from app.core.db import get_db_session
from fastapi import Depends
from sqlalchemy.orm import Session


SessionDepends = Annotated[Session, Depends(get_db_session)]
