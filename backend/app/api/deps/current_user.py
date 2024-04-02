from typing import Annotated

from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt

from app.api.deps.crud import CrudUserDepends
from shared.database.models import User

ouath_sceheme = OAuth2PasswordBearer(tokenUrl="token")


async def get_current_user(
    token: Annotated[str, Depends(ouath_sceheme)],
    user_crud: CrudUserDepends,
) -> User:
    try:
        if (user := await user_crud.get(int(token))) is not None:
            return user
    except ValueError:
        pass

    try:
        payload = jwt.decode(
            token, "LcH6ouNfUvAhn4AdmjkwkvfzbUHn3ViVHqjt8P1umPc", algorithms=["HS256"]
        )
        user_id: int = int(payload.get("sub"))
        if user_id is None:
            raise HTTPException(401, detail="Wrong credentials")
    except JWTError:
        raise HTTPException(401, detail="Wrong credentials")
    user = await user_crud.get(user_id)
    if user is None:
        raise HTTPException(401, detail="Wrong credentials")
    return user


CurrentUserDep = Annotated[User, Depends(get_current_user)]
