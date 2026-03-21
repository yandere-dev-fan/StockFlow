from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.modules.organizations import service
from app.modules.organizations.schemas import (
    OrganizationCreate,
    OrganizationUpdate,
    OrganizationResponse
)

router = APIRouter(prefix="/organizations", tags=["organizations"])


@router.get("/", response_model=list[OrganizationResponse])
def get_organizations(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    return service.get_organizations(db=db, skip=skip, limit=limit)


@router.get("/{org_id}", response_model=OrganizationResponse)
def get_organization(org_id: UUID, db: Session = Depends(get_db)):
    org = service.get_organization(db=db, org_id=org_id)
    if not org:
        raise HTTPException(status_code=404, detail="Organization not found")
    return org


@router.post("/", response_model=OrganizationResponse)
def create_organization(
    data: OrganizationCreate,
    db: Session = Depends(get_db)
):
    return service.create_organization(db=db, data=data)


@router.put("/{org_id}", response_model=OrganizationResponse)
def update_organization(
    org_id: UUID,
    data: OrganizationUpdate,
    db: Session = Depends(get_db)
):
    org = service.update_organization(db=db, org_id=org_id, data=data)
    if not org:
        raise HTTPException(status_code=404, detail="Organization not found")
    return org


@router.delete("/{org_id}")
def delete_organization(org_id: UUID, db: Session = Depends(get_db)):
    success = service.delete_organization(db=db, org_id=org_id)
    if not success:
        raise HTTPException(status_code=404, detail="Organization not found")
    return {"status": "ok"}