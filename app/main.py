from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.db import db_helper
from app.api.v1 import router


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield

    await db_helper.dispose()


app = FastAPI(title="Ticketing System", lifespan=lifespan)

app.include_router(router)
