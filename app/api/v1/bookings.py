from fastapi import APIRouter

from .deps import SessionDep
from app.schemas.booking import BookingResponse, BookingCreate
from app.services.booking import BookingService


router = APIRouter(prefix="/bookings", tags=["bookings"])
service = BookingService()


@router.get("/", response_model=list[BookingResponse])
async def get_bookings(session: SessionDep):
    return await service.get_all(session)


@router.post("/", response_model=BookingResponse)
async def create_booking(booking: BookingCreate, session: SessionDep):
    return await service.book_ticket(session, booking.user_id, booking.event_id)


@router.get("/{booking_id}", response_model=BookingResponse)
async def get_booking(booking_id: int, session: SessionDep):
    return await service.get(session, booking_id)
