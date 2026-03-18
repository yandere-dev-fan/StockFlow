from datetime import datetime
from uuid import UUID
from pydantic import BaseModel


class LocationCreate(BaseModel):
    name: str
    level: str
    parent_id: UUID | None = None


class LocationUpdate(BaseModel):
    name: str | None = None
    level: str | None = None
    parent_id: UUID | None = None


class LocationParent(BaseModel):
    id: UUID
    name: str
    level: str

    class Config:
        from_attributes = True


class LocationResponse(BaseModel):
    id: UUID
    org_id: UUID
    name: str
    level: str
    parent_id: UUID | None
    parent: LocationParent | None
    created_at: datetime

    class Config:
        from_attributes = True