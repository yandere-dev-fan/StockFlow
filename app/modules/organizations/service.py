# app/modules/organizations/service.py

from uuid import UUID
from sqlalchemy.orm import Session
from app.modules.organizations.models import Organization
from app.modules.organizations.schemas import OrganizationCreate, OrganizationUpdate


def get_organization(db: Session, org_id: UUID) -> Organization | None:
    return db.query(Organization)\
             .filter(Organization.id == org_id,
                     Organization.is_active == True)\
             .first()


def get_organizations(db: Session, skip: int = 0, limit: int = 100) -> list[Organization]:
    return db.query(Organization)\
             .filter(Organization.is_active == True)\
             .order_by(Organization.created_at.desc())\
             .offset(skip)\
             .limit(limit)\
             .all()


def create_organization(db: Session, data: OrganizationCreate) -> Organization:
    org = Organization(
        name=data.name,
        slug=data.slug,
        plan=data.plan,
        website_url=data.website_url,
        billing_email=data.billing_email,
        logo_url=data.logo_url
    )
    db.add(org)
    db.commit()
    db.refresh(org)
    return org


def update_organization(db: Session, org_id: UUID, data: OrganizationUpdate) -> Organization | None:
    org = get_organization(db=db, org_id=org_id)
    if not org:
        return None
    for field, value in data.model_dump(exclude_unset=True).items():
        setattr(org, field, value)
    db.commit()
    db.refresh(org)
    return org


def delete_organization(db: Session, org_id: UUID) -> bool:
    org = get_organization(db=db, org_id=org_id)
    if not org:
        return False
    org.is_active = False
    db.commit()
    return True