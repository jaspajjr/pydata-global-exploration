from fastapi import APIRouter, HTTPException

from models import Organiser

router = APIRouter(prefix="/organisers", tags=["organisers"])

_organisers: dict[str, Organiser] = {}


@router.post("", response_model=Organiser, status_code=201)
def create_organiser(organiser: Organiser):
    _organisers[organiser.organiser_id] = organiser
    return organiser


@router.get("", response_model=list[Organiser])
def list_organisers():
    return list(_organisers.values())


@router.get("/{organiser_id}", response_model=Organiser)
def get_organiser(organiser_id: str):
    if organiser_id not in _organisers:
        raise HTTPException(status_code=404, detail="Organiser not found")
    return _organisers[organiser_id]


@router.put("/{organiser_id}", response_model=Organiser)
def update_organiser(organiser_id: str, organiser: Organiser):
    if organiser_id not in _organisers:
        raise HTTPException(status_code=404, detail="Organiser not found")
    _organisers[organiser_id] = organiser
    return organiser


@router.delete("/{organiser_id}", status_code=204)
def delete_organiser(organiser_id: str):
    if organiser_id not in _organisers:
        raise HTTPException(status_code=404, detail="Organiser not found")
    del _organisers[organiser_id]
