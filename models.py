from uuid import uuid4

from pydantic import BaseModel, Field


class Organiser(BaseModel):
    organiser_id: str = Field(default_factory=lambda: str(uuid4()))
    name: str
    email: str
    linkedin: str
    photo: str


class Meetup(BaseModel):
    meetup_id: str = Field(default_factory=lambda: str(uuid4()))
    name: str
    city: str
    chapter_email: str
    google_group: str
    organisers: list[str]
