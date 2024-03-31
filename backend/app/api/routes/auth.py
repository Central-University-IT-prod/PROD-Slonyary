from fastapi import APIRouter, HTTPException, status

from app.core import security
from app.crud import CrudUserDepends
from app.schemas import UserCreate, UserTelegramData

router = APIRouter()


@router.post("/", status_code=200)
async def auth_user(
    user_telegram_data_hash: str,
    user_telegram_data: UserTelegramData,
    user_crud: CrudUserDepends,
) -> dict:
    """
    Регистрация пользователя в системе.
    Для регистрация отправляются данные о его тг аккаунте и хэш для проверки валидности.
    Данные от аккаунта хешируются с ключом бота и сравниваются с хэшом для проверки.
    Переданные данные в json конвертируются в строку с добавлением \n.

    Parameters:
        user_telegram_data_hash: str - хэш для проверки.
        user_telegram_data: UserTelegramData - данные пользователя от телеграм-аккаунта.
        user_crud:

    Returns:
        {"status": "ok"}

    Errors:
        400 - проблемы валидации pyndatic
        401 - данные не прошли проверку
    """
    data_check_list = []

    user_data_dict = user_telegram_data.model_dump()
    for key, value in sorted(user_data_dict.items()):  # Sort required!
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
                telegram_id=user_telegram_data.id,
                username=user_telegram_data.username,
                name=user_telegram_data.first_name,
            ),
        )

    return {"status": "ok"}
