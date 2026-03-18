from datetime import datetime
from uuid import UUID
from typing import Literal
from pydantic import BaseModel

# Статусы вынесем отдельно чтобы не повторять дважды
ItemStatus = Literal[
    "listed", "unlisted", "sold",
    "being_delivered_to_warehouse",
    "delivered_to_warehouse",
    "being_delivered_to_client",
    "delivered_to_client"
]


class ItemUnitCreate(BaseModel):
    attributes: dict = {}

class ItemUnitResponse(BaseModel):
    id: UUID
    item_id: UUID
    attributes: dict
    status: ItemStatus
    created_at: datetime

    class Config:
        from_attributes = True


class ItemCreate(BaseModel):
    item_type_id: UUID
    location_id: UUID | None = None
    sku: str
    attributes: dict = {}
    photos: list[str] = []
    purchase_price: float | None = None
    retail_price: float
    is_bulk: bool = False
    stock_qty: int = 1
    markdown_eligible: bool = False


class ItemUpdate(BaseModel):
    location_id: UUID | None = None
    sku: str | None = None
    attributes: dict | None = None
    photos: list[str] | None = None
    purchase_price: float | None = None
    retail_price: float | None = None
    is_bulk: bool | None = None
    stock_qty: int | None = None
    markdown_eligible: bool | None = None
    status: ItemStatus | None = None


class ItemResponse(BaseModel):
    id: UUID
    org_id: UUID
    item_type_id: UUID
    location_id: UUID | None
    sku: str
    attributes: dict
    photos: list[str]
    purchase_price: float | None
    retail_price: float
    is_bulk: bool
    stock_qty: int
    markdown_eligible: bool
    status: ItemStatus
    last_sold_at: datetime | None
    created_at: datetime
    units: list[ItemUnitResponse] = []

    class Config:
        from_attributes = True