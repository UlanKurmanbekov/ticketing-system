from fastapi import APIRouter

from .bookings import router as booking_router
from .events import router as event_router
from .users import router as user_router


router = APIRouter()

router.include_router(booking_router)
router.include_router(event_router)
router.include_router(user_router)
