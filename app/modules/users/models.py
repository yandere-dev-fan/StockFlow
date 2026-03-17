from sqlalchemy import Column, String, Boolean, DateTime, Enum, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
import uuid
from app.modules.organizations.models import OrgMember
from app.database import Base

class User(Base):
    __tablename__ = "users"

    id            = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name          = Column(String(255), nullable=False)
    email         = Column(String, nullable=False, unique=True)
    password_hash = Column(String, nullable=False)
    created_at    = Column(DateTime, server_default=func.now())
    memberships   = relationship("OrgMember", back_populates="user")