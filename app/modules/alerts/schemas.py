from datetime import datetime
from uuid import UUID
from typing import Literal
from pydantic import BaseModel

AlertStatus = Literal["pending", "read", "dismissed"]


class AlertRuleCreate(BaseModel):
    item_type_id: UUID
    day_count: int
    message_template: str
    is_active: bool = True


class AlertRuleUpdate(BaseModel):
    item_type_id: UUID | None = None
    day_count: int | None = None
    message_template: str | None = None
    is_active: bool | None = None


class AlertRuleResponse(BaseModel):
    id: UUID
    org_id: UUID
    item_type_id: UUID
    day_count: int
    message_template: str
    is_active: bool
    created_at: datetime

    class Config:
        from_attributes = True


class AlertResponse(BaseModel):
    id: UUID
    item_id: UUID
    alert_rule_id: UUID
    status: AlertStatus
    created_at: datetime

    class Config:
        from_attributes = True


class AlertUpdate(BaseModel):
    status: AlertStatus | None = None