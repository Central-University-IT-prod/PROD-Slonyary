from datetime import timedelta, timezone, datetime

from app.api.deps import CrudUserDepends
from app.core import security
from app.schemas import UserCreate, UserTelegramData
from fastapi import APIRouter, HTTPException, status
from jose import jwt

router = APIRouter()


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(
        to_encode, "LcH6ouNfUvAhn4AdmjkwkvfzbUHn3ViVHqjt8P1umPc", algorithm="HS256"
    )
    return encoded_jwt


@router.post("/", status_code=200)
async def auth_user(
    user_telegram_data: UserTelegramData,
    user_crud: CrudUserDepends,
) -> dict:
    """
    Регистрация пользователя в системе.
    Для регистрация отправляются данные о его тг аккаунте и хэш для проверки валидности.
    Данные от аккаунта хешируются с ключом бота и сравниваются с хэшом для проверки.
    Переданные данные в json конвертируются в строку с добавлением \n.

    Parameters:
        user_telegram_data: UserTelegramData - данные пользователя от телеграм-аккаунта.
        user_crud:

    Returns:
        {"token": "jwt"}

    Errors:
        400 - проблемы валидации pyndatic
        401 - данные не прошли проверку
    """
    user_telegram_data_hash = user_telegram_data.hash
    data_check_list = []

    user_data_dict = user_telegram_data.model_dump()
    for key, value in sorted(user_data_dict.items()):  # Sort required!
        if key != "hash" and value != None:
            data_check_list.append(f"{key}={value}")

    data_check_string = "\n".join(data_check_list)
    is_valid = security.verify_user_data(data_check_string, user_telegram_data_hash)

    if not is_valid:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Данные неверны",
        )

    is_user = await user_crud.is_exists(telegram_id=user_telegram_data.id)

    # Добавляем пользователя в базу, елси он авторизовывается впервые.
    if not is_user:
        await user_crud.create(
            UserCreate(
                id=user_telegram_data.id,
                username=user_telegram_data.username,
                name=user_telegram_data.first_name,
            ),
        )

    access_token_expires = timedelta(minutes=180)
    access_token = create_access_token(
        data={"sub": str(user_telegram_data.id)}, expires_delta=access_token_expires
    )
    return {"token": access_token}
