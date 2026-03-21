from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from uuid import UUID
from app.database import get_db
from app.modules.locations import service
from app.modules.locations.schemas import LocationCreate, LocationUpdate, LocationResponse

router = APIRouter(prefix="/locations", tags=["locations"])


@router.get("/", response_model=list[LocationResponse])
def get_locations(
    org_id: UUID,
    parent_id: UUID | None = None,
    db: Session = Depends(get_db)
):
    return service.get_locations(db=db, org_id=org_id, parent_id=parent_id)


@router.get("/{location_id}", response_model=LocationResponse)
def get_location(location_id: UUID, db: Session = Depends(get_db)):
    loc = service.get_location(db=db, location_id=location_id)
    if not loc:
        raise HTTPException(status_code=404, detail="Location not found")
    return loc


@router.post("/", response_model=LocationResponse)
def create_location(
    org_id: UUID,
    data: LocationCreate,
    db: Session = Depends(get_db)
):
    return service.create_location(db=db, org_id=org_id, data=data)


@router.put("/{location_id}", response_model=LocationResponse)
def update_location(
    location_id: UUID,
    data: LocationUpdate,
    db: Session = Depends(get_db)
):
    loc = service.update_location(db=db, location_id=location_id, data=data)
    if not loc:
        raise HTTPException(status_code=404, detail="Location not found")
    return loc


@router.delete("/{location_id}")
def delete_location(location_id: UUID, db: Session = Depends(get_db)):
    success = service.delete_location(db=db, location_id=location_id)
    if not success:
        raise HTTPException(status_code=404, detail="Location not found")
    return {"status": "ok"}

@router.get("/{location_id}/path", response_model=list[LocationResponse])
def get_location_path(location_id: UUID, db: Session = Depends(get_db)):
    path = service.get_location_path(db=db, location_id=location_id)
    if not path:
        raise HTTPException(status_code=404, detail="Location not found")
    return path


@router.get("/{location_id}/children", response_model=list[LocationResponse])
def get_all_children(
    location_id: UUID,
    db: Session = Depends(get_db)
):
    return service.get_locations(db=db, parent_id=location_id)


@router.put("/{location_id}/move", response_model=LocationResponse)
def move_location(
    location_id: UUID,
    new_parent_id: UUID | None = None,
    db: Session = Depends(get_db)
):
    loc = service.move_location(db=db, location_id=location_id, new_parent_id=new_parent_id)
    if not loc:
        raise HTTPException(status_code=404, detail="Location not found")
    return loc