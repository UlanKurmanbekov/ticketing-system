from fastapi import APIRouter

from .deps import SessionDep
from app.schemas.user import UserResponse
from app.services.user import UserService


router = APIRouter(prefix='/users', tags=['users'])
service = UserService()


@router.get('/', response_model=list[UserResponse])
async def get_users(session: SessionDep):
    return await service.get_all(session)


@router.post('/', response_model=UserResponse)
async def create_user(session: SessionDep):
    return await service.create(session)

