"""Config file for some environment settings."""
import logging
import os
from functools import lru_cache

from pydantic import BaseSettings

log = logging.getLogger("uvicorn")


class Settings(BaseSettings):
    """Set Environment Settings."""

    environment: str = os.getenv("ENVIRONMENT", "dev")
    testing: bool = os.getenv("TESTING", 0)


@lru_cache()
def get_settings() -> BaseSettings:
    """Retrieve Settings."""
    log.info("Loading config settings from the environment...")
    return Settings()
