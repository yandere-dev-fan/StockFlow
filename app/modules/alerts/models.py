from sqlalchemy import Column, String, Boolean, DateTime, Integer, Enum, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
import uuid
from app.database import Base
from app.core.enums import alert_status_enum

class AlertRule(Base):
    __tablename__ = "alert_rules"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    org_id = Column(UUID(as_uuid=True), ForeignKey("organizations.id"), nullable=False)
    item_type_id = Column(UUID(as_uuid=True), ForeignKey("item_types.id"), nullable=False)
    day_count = Column(Integer, nullable=False)
    message_template = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, server_default=func.now())

    organization = relationship("Organization", back_populates="alert_rules")
    item_type = relationship("ItemType", back_populates="alert_rules")
    alerts = relationship("Alert", back_populates="alert_rule")

class Alert(Base):
    __tablename__ = "alerts"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    item_id = Column(UUID(as_uuid=True), ForeignKey("items.id"), nullable=False)
    alert_rule_id = Column(UUID(as_uuid=True), ForeignKey("alert_rules.id"))
    status = Column(alert_status_enum, nullable=False, default="pending")
    created_at = Column(DateTime, server_default=func.now())

    item = relationship("Item", back_populates="alerts")
    alert_rule = relationship("AlertRule", back_populates="alerts")
