from typing import Generic, Type, TypeVar, Union

import sqlalchemy
from app.core.db import Base
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from sqlalchemy.orm import Session

ModelType = TypeVar("ModelType", bound=Base)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
# TODO: update schema support.
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


class CrudBase(Generic[ModelType, CreateSchemaType]):
    def __init__(self, Model: Type[ModelType]):
        """
        CRUD object with default methods to Create, Read, Update, Delete (CRUD).

        **Parameters**

        * `model`: A SQLAlchemy model class
        * `schema`: A Pydantic model (schema) class
        """
        self.Model = Model

    async def get(self, db: Session, id: int) -> Union[ModelType, None]:
        """
        Get query by id.
        Error will be raised if entity doesn't have id column.
        """
        try:
            query = sqlalchemy.select(self.Model).where(self.Model.id == id)
            result = await db.scalar(query)
            return result
        except AttributeError as e:
            print(f"Error: {e}")
            return None

    async def create(self, db: Session, obj_in: CreateSchemaType) -> ModelType:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.Model(**obj_in_data)  # type: ignore
        db.add(db_obj)
        await db.commit()
        await db.refresh(db_obj)
        return db_obj

    async def update(
        self, db: Session, db_obj: ModelType, obj_in: UpdateSchemaType
    ) -> ModelType:
        obj_data = jsonable_encoder(db_obj)
        update_data = obj_in.model_dump(exclude_unset=True)
        for field in obj_data:
            if field in update_data:
                setattr(db_obj, field, update_data[field])
        db.add(db_obj)
        await db.commit()
        await db.refresh(db_obj)
        return db_obj

    async def delete(self, db: Session, id: int) -> ModelType:
        obj = await self.get(db, id)
        db.delete(obj)
        await db.commit()
        return obj
