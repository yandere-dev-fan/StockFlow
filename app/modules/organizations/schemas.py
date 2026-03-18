from datetime import datetime
from uuid import UUID
from pydantic import BaseModel


class OrganizationCreate(BaseModel):
    name: str
    slug: str
    plan: str = "free"
    website_url: str | None = None
    billing_email: str | None = None
    logo_url: str | None = None


class OrganizationUpdate(BaseModel):
    name: str | None = None
    slug: str | None = None
    plan: str | None = None
    website_url: str | None = None
    billing_email: str | None = None
    logo_url: str | None = None


class OrganizationResponse(BaseModel):
    id: UUID
    name: str
    slug: str
    plan: str
    is_active: bool
    created_at: datetime

    class Config:
        from_attributes = True