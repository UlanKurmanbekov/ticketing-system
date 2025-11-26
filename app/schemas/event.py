from pydantic import BaseModel, ConfigDict


class EventCreate(BaseModel):
    name: str
    total_tickets: int


class EventResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    total_tickets: int
    sold_tickets: int
