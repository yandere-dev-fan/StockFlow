from sqlalchemy.orm import Session
from uuid import UUID
from app.modules.locations.models import Location
from app.modules.locations.schemas import LocationCreate, LocationUpdate


def get_location(db: Session, location_id: UUID) -> Location | None:
    return db.query(Location)\
             .filter(Location.id == location_id)\
             .first()


def get_locations(db: Session, org_id: UUID, parent_id: UUID | None = None) -> list[Location]:
    query = db.query(Location).filter(Location.org_id == org_id)
    if parent_id:
        query = query.filter(Location.parent_id == parent_id)
    else:
        query = query.filter(Location.parent_id == None)
    return query.all()


def create_location(db: Session, org_id: UUID, data: LocationCreate) -> Location:
    loc = Location(
        org_id=org_id,
        name=data.name,
        level=data.level,
        parent_id=data.parent_id
    )
    db.add(loc)
    db.commit()
    db.refresh(loc)
    return loc


def update_location(db: Session, location_id: UUID, data: LocationUpdate) -> Location | None:
    loc = get_location(db=db, location_id=location_id)
    if not loc:
        return None
    for field, value in data.model_dump(exclude_unset=True).items():
        setattr(loc, field, value)
    db.commit()
    db.refresh(loc)
    return loc


def delete_location(db: Session, location_id: UUID) -> bool:
    loc = get_location(db=db, location_id=location_id)
    if not loc:
        return False
    db.delete(loc)
    db.commit()
    return True

def get_location_path(db: Session, location_id: UUID) -> list[Location]:
    path = []
    current = get_location(db, location_id)
    while current:
        path.append(current)
        current = get_location(db, current.parent_id) if current.parent_id else None
    return list(reversed(path))

def get_all_children(db: Session, location_id: UUID) -> list[Location]:
    result = []
    children = db.query(Location)\
                 .filter(Location.parent_id == location_id)\
                 .all()
    for child in children:
        result.append(child)
        result.extend(get_all_children(db, child.id))
    return result

def move_location(db: Session, location_id: UUID, new_parent_id: UUID | None) -> Location | None:
    loc = get_location(db, location_id)
    if not loc:
        return None
    loc.parent_id = new_parent_id
    db.commit()
    db.refresh(loc)
    return loc