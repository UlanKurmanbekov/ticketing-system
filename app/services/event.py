from typing import Sequence

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException

from app.models import Event


class EventService:
    async def get_all(self, session: AsyncSession) -> Sequence[Event]:
        stmt = select(Event)
        result = await session.execute(stmt)

        return result.scalars().all()

    async def create_event(self, session: AsyncSession, name: str, total_tickets: int) -> Event:
        event = Event(name=name, total_tickets=total_tickets)
        session.add(event)
        await session.commit()

        return event

    async def get(self, session: AsyncSession, event_id: int) -> Event:
        stmt = select(Event).where(Event.id == event_id)
        result = await session.execute(stmt)
        event = result.scalar_one_or_none()

        if event is None:
            raise HTTPException(404, "Event not found")

        return event
