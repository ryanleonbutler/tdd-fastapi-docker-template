import uvicorn
from fastapi import Depends, FastAPI

from api.config import Settings, get_settings

api = FastAPI()


@api.get("/")
async def pong(settings: Settings = Depends(get_settings)):
    return {
        "Ping": "Pong",
        "environment": settings.environment,
        "testing": settings.testing,
    }


if __name__ == "__main__":
    uvicorn.run(api, port=8000, host="127.0.0.1", reload=True)
