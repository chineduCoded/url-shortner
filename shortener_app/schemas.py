#!/usr/bin/python3
"""Defines URLBase, URL, URLInfo classes"""
from pydantic import BaseModel


class URLBase(BaseModel):
    """Inherits from BaseModel Class"""
    target_url: str

    class Config:
        orm_mode = True


class URL(URLBase):
    """Inherits from URLBase Classs"""
    is_active: bool
    clicks: int


class URLInfo(URL):
    """Inherits from URL Class"""
    url: str
    admin_url: str
