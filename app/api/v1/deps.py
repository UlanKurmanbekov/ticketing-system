from typing import Annotated, AsyncGenerator

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.helper import db_helper


async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async for session in db_helper.get_session():
        yield session

SessionDep = Annotated[AsyncSession, Depends(get_session)]
