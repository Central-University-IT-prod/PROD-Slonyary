import asyncio

from shared.database.models.base import AlchemyBaseModel
from shared.database.session import db_engine


async def main() -> None:
    async with db_engine.begin() as conn:
        await conn.run_sync(AlchemyBaseModel.metadata.create_all)


if __name__ == "__main__":
    asyncio.run(main())
