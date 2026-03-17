from sqlalchemy import Column, String, Boolean, DateTime, Enum, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
import uuid
from app.modules.organizations.models import OrgMember, Organization
from app.modules.users.models import User
from app.database import Base

class Location(Base):
    __tablename__ = "locations"

    id         = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    org_id     = Column(UUID(as_uuid=True), ForeignKey("organizations.id"), nullable=False)
    parent_id  = Column(UUID(as_uuid=True), ForeignKey("locations.id"), nullable=True)
    name       = Column(String(255), nullable=False)
    level      = Column(Enum("warehouse", "room", "rack", "shelf", "slot", name="location_level"), nullable=False)
    created_at = Column(DateTime, server_default=func.now())

    organization = relationship("Organization", back_populates="locations")
    parent       = relationship("Location", back_populates="children", remote_side="Location.id")
    children     = relationship("Location", back_populates="parent")
    items = relationship("Item", back_populates="location")