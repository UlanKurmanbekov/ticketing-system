from typing import Sequence

from sqlalchemy import select, update, exists
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException

from app.models import Event, Booking


class BookingService:
    async def get_all(self, session: AsyncSession) -> Sequence[Booking]:
        stmt = select(Booking)
        result = await session.execute(stmt)

        return result.scalars().all()

    async def book_ticket(self, session: AsyncSession, user_id: int, event_id: int) -> Booking:
        stmt = update(Event).where(
            Event.id == event_id,
            Event.sold_tickets < Event.total_tickets
        ).values(sold_tickets=Event.sold_tickets + 1).returning(Event.id)

        result = await session.execute(stmt)
        updated_event_id = result.scalar_one_or_none()

        if updated_event_id is None:
            result = await session.execute(
                select(exists().where(Event.id == event_id))
            )
            if not result.scalar():
                raise HTTPException(404, "Event not found")
            raise HTTPException(400, "Sold out")

        booking = Booking(user_id=user_id, event_id=event_id)
        session.add(booking)

        try:
            await session.commit()
        except IntegrityError:
            raise HTTPException(400, "Already booked")

        return booking

    async def get(self, session: AsyncSession, booking_id: int) -> Booking:
        stmt = select(Booking).where(Booking.id == booking_id)
        result = await session.execute(stmt)
        result = result.scalar_one_or_none()

        if result is None:
            raise HTTPException(404, "Booking not found")

        return result
