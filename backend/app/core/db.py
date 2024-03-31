from typing import Any

from app.core.config import settings
from sqlalchemy import MetaData
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker, Session
from sqlalchemy.orm.exc import DetachedInstanceError


class Base(DeclarativeBase):
    """Базовый класс для моделей Алхимии. Реализует удобный вывод для дебага."""

    __abstract__ = True

    metadata = MetaData(
        naming_convention={
            "ix": "ix_%(column_0_label)s",
            "uq": "uq_%(table_name)s_%(column_0_name)s",
            "ck": "ck_%(table_name)s_%(constraint_name)s",
            "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
            "pk": "pk_%(table_name)s",
        },
    )

    def __repr__(self) -> str:
        """Вывод информации о моделе в человекочитаемом виде."""
        return self._repr(
            **{c.name: getattr(self, c.name) for c in self.__table__.columns}  # noqa
        )

    def _repr(self, **fields: Any) -> str:
        """
        Помощник __repr__.

        Взят с https://stackoverflow.com/a/55749579
        """
        field_strings = []
        at_least_one_attached_attribute = False

        for key, field in fields.items():
            try:
                field_strings.append(f"{key}={field!r}")
            except DetachedInstanceError:
                field_strings.append(f"{key}=DetachedInstanceError")
            else:
                at_least_one_attached_attribute = True

        if at_least_one_attached_attribute:
            return f"<{self.__class__.__name__}({', '.join(field_strings)})>"
        return f"<{self.__class__.__name__} {id(self)}>"


engine = create_async_engine(str(settings.SQLALCHEMY_DATABASE_URI))
SessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine, class_=AsyncSession
)


# make sure all SQLModel models are imported (app.models) before initializing DB
# otherwise, SQLModel might fail to initialize relationships properly
# for more details: https://github.com/tiangolo/full-stack-fastapi-template/issues/28


def init_db(session: Session) -> None:
    # Tables should be created with Alembic migrations
    # But if you don't want to use migrations, create
    # the tables un-commenting the next lines
    # from sqlmodel import SQLModel

    # from app.core.engine import engine
    # This works because the models are already imported and registered from app.models
    # SQLModel.metadata.create_all(engine)
    from app.models import User
    from app.schemas import UserCreate

    # TODO: superuser registration
