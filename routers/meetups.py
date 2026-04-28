from fastapi import APIRouter, HTTPException

from models import Meetup

router = APIRouter(prefix="/meetups", tags=["meetups"])

_meetups: dict[str, Meetup] = {}


@router.post("", response_model=Meetup, status_code=201)
def create_meetup(meetup: Meetup):
    if meetup.meetup_id in _meetups:
        raise HTTPException(status_code=409, detail="Meetup already exists")
    _meetups[meetup.meetup_id] = meetup
    return meetup


@router.get("", response_model=list[Meetup])
def list_meetups():
    return list(_meetups.values())


@router.get("/{meetup_id}", response_model=Meetup)
def get_meetup(meetup_id: str):
    if meetup_id not in _meetups:
        raise HTTPException(status_code=404, detail="Meetup not found")
    return _meetups[meetup_id]


@router.put("/{meetup_id}", response_model=Meetup)
def update_meetup(meetup_id: str, meetup: Meetup):
    if meetup_id not in _meetups:
        raise HTTPException(status_code=404, detail="Meetup not found")
    _meetups[meetup_id] = meetup
    return meetup


@router.delete("/{meetup_id}", status_code=204)
def delete_meetup(meetup_id: str):
    if meetup_id not in _meetups:
        raise HTTPException(status_code=404, detail="Meetup not found")
    del _meetups[meetup_id]
