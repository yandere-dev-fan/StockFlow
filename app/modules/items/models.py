from email.policy import default

from sqlalchemy import Column, String, Boolean, DateTime, Enum, ForeignKey, Numeric, Integer
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
import uuid
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.ext.declarative import declarative_base
from app.modules.organizations.models import OrgMember, Organization
from app.modules.users.models import User
from app.database import Base

class Item(Base):
    __tablename__ = "items"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    org_id = Column(UUID(as_uuid=True), ForeignKey("organizations.id"), nullable=False)
    item_type_id = Column(UUID(as_uuid=True), ForeignKey("item_types.id"), nullable=False)
    location_id = Column(UUID(as_uuid=True), ForeignKey("locations.id"), nullable=True)
    sku = Column(String(100), nullable=False, unique=True)
    attributes = Column(JSONB, nullable=False, default=dict)
    photos = Column(JSONB, default=list)
    purchase_price = Column(Numeric(precision=10, scale=2), nullable=True)
    retail_price = Column(Numeric(precision=10, scale=2), nullable=False)
    is_bulk = Column(Boolean, default=False, nullable=False)
    stock_qty = Column(Integer, default=1, nullable=False)
    markdown_eligible = Column(Boolean, default=False)
    status = Column(
        Enum(
            "listed", "unlisted", "sold",
            "being_delivered_to_warehouse",
            "delivered_to_warehouse",
            "being_delivered_to_client",
            "delivered_to_client",
            name="item_status"
        ),
        default="unlisted",
        nullable=False
    )
    organization = relationship("Organization", back_populates="items")
    item_type = relationship("ItemType", back_populates="items")
    location = relationship("Location", back_populates="items")
    units = relationship("ItemUnit", back_populates="item")
    alerts = relationship("Alert", back_populates="item")

class ItemType(Base):
    __tablename__ = "item_types"

    id            = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    org_id        = Column(UUID(as_uuid=True), ForeignKey("organizations.id"), nullable=False)
    name          = Column(String(255), nullable=False)
    fields_schema = Column(JSONB, nullable=False, default=list)
    created_at    = Column(DateTime, server_default=func.now())

    organization = relationship("Organization", back_populates="item_types")
    items = relationship("Item", back_populates="item_type")
    alert_rules = relationship("AlertRule", back_populates="item_type")

class ItemUnit(Base):
    __tablename__ = "item_units"

    id         = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    item_id    = Column(UUID(as_uuid=True), ForeignKey("items.id"), nullable=False)
    attributes = Column(JSONB, nullable=False, default=dict)
    status     = Column(
        Enum(
            "listed", "unlisted", "sold",
            "being_delivered_to_warehouse",
            "delivered_to_warehouse",
            "being_delivered_to_client",
            "delivered_to_client",
            name="item_status"
        ),
        default="unlisted",
        nullable=False
    )
    created_at = Column(DateTime, server_default=func.now())
    item = relationship("Item", back_populates="units")