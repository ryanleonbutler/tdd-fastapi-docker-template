import os

from api.config import Settings, get_settings
from fastapi import Depends, FastAPI
from tortoise.contrib.fastapi import register_tortoise

api = FastAPI()


register_tortoise(
    api,
    db_url=os.environ.get("DATABASE_URL"),
    modules={"models": ["api.models.tortoise"]},
    generate_schemas=True,
    add_exception_handlers=True,
)


@api.get("/ping")
async def pong(settings: Settings = Depends(get_settings)):
    return {
        "Ping": "Pong",
        "environment": settings.environment,
        "testing": settings.testing,
    }
