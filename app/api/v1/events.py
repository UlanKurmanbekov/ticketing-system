from fastapi import APIRouter

from .deps import SessionDep
from app.schemas.event import EventResponse, EventCreate
from app.services.event import EventService


router = APIRouter(prefix='/events', tags=['events'])
service = EventService()


@router.get('/', response_model=list[EventResponse])
async def get_events(session: SessionDep):
    return await service.get_all(session)


@router.post('/', response_model=EventResponse)
async def create_event(session: SessionDep, event: EventCreate):
    return await service.create_event(session, event.name, event.total_tickets)


@router.get('/{event_id}', response_model=EventResponse)
async def get_event(session: SessionDep, event_id: int):
    return await service.get(session, event_id)
