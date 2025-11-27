from typing import Sequence

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import User


class UserService:
    async def get_all(self, session: AsyncSession) -> Sequence[User]:
        stmt = select(User)
        result = await session.execute(stmt)

        return result.scalars().all()

    async def create(self, session: AsyncSession) -> User:
        user = User()
        session.add(user)
        await session.commit()

        return user
