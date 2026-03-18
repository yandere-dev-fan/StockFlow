from sqlalchemy import Column, String, Boolean, DateTime, Enum, ForeignKey, Numeric
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
import uuid
from app.database import Base

class Sale(Base):
    __tablename__ = "sales"

    id             = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    org_id         = Column(UUID(as_uuid=True), ForeignKey("organizations.id"), nullable=False)
    item_id        = Column(UUID(as_uuid=True), ForeignKey("items.id"), nullable=False)
    sold_price     = Column(Numeric(precision=10, scale=2), nullable=False)
    purchase_price = Column(Numeric(precision=10, scale=2), nullable=False)
    sold_at        = Column(DateTime, server_default=func.now(), nullable=False)

    organization = relationship("Organization", back_populates="sales")
    item         = relationship("Item", back_populates="sales")