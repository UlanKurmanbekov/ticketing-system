from fastapi import APIRouter

from .bookings import router as booking_router
from .events import router as event_router


router = APIRouter()

router.include_router(booking_router)
router.include_router(event_router)
