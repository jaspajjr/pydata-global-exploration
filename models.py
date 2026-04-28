from pydantic import BaseModel


class Organiser(BaseModel):
    organiser_id: str
    name: str
    email: str
    linkedin: str
    photo: str


class Meetup(BaseModel):
    meetup_id: str
    name: str
    city: str
    chapter_email: str
    google_group: str
    organisers: list[str]
