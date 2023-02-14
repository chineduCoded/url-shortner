#!/usr/bin/python3
"""Defines Settings Class"""
from functools import lru_cache

from pydantic import BaseSettings


class Settings(BaseSettings):
    """Represent env settings"""
    env_name: str = "Local"
    base_url: str = "http://localhost:8000"
    db_url: str = "sqlite:///./shortener.db"

    class Config:
        env_file = ".env"

@lru_cache
def get_settings() -> Settings:
    """
    Gets settings.
    Optimized by LRU cache strategy
    LRU - Last Recently Used
    """
    settings = Settings()
    print(f"Loading settings for: {settings.env_name}")
    return settings
