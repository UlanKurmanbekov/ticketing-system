from sqlalchemy import String
from sqlalchemy.orm import mapped_column, Mapped

from .base import Base


class Event(Base):
    __tablename__ = 'events'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(256))
    total_tickets: Mapped[int] = mapped_column()
    sold_tickets: Mapped[int] = mapped_column(default=0)
