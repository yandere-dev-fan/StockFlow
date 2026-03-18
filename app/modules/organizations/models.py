from sqlalchemy import Column, String, Boolean, DateTime, Enum, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
import uuid
from app.database import Base

class Organization(Base):
    __tablename__ = "organizations"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String(255), nullable=False)
    slug = Column(String, nullable=False, unique=True)
    is_active = Column(Boolean, default=True)
    plan = Column(Enum("free", "pro", "enterprise", name="plan_type"), default="free")
    website_url = Column(String, nullable=True)
    billing_email = Column(String, nullable=True)
    logo_url = Column(String, nullable=True)
    created_at = Column(DateTime, server_default=func.now())

    members = relationship("OrgMember", back_populates="organization")
    locations = relationship("Location", back_populates="organization")
    item_types = relationship("ItemType", back_populates="organization")
    alert_rules = relationship("AlertRule", back_populates="organization")
    items = relationship("Item", back_populates="organization")

class OrgMember(Base):
    __tablename__ = "org_members"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    org_id = Column(UUID(as_uuid=True), ForeignKey("organizations.id"), nullable=False)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    role = Column(Enum("owner", "manager", "staff", name="role_type"), default="staff")
    created_at = Column(DateTime, server_default=func.now())

    organization = relationship("Organization", back_populates="members")
    user         = relationship("User", back_populates="memberships")
    locations = relationship("Location", back_populates="organization")
