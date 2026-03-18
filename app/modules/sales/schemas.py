from datetime import datetime
from uuid import UUID
from pydantic import BaseModel, computed_field


class SaleCreate(BaseModel):
    item_id: UUID
    sold_price: float
    purchase_price: float


class SaleResponse(BaseModel):
    id: UUID
    org_id: UUID
    item_id: UUID
    sold_price: float
    purchase_price: float
    sold_at: datetime

    @computed_field
    @property
    def profit(self) -> float:
        return round(self.sold_price - self.purchase_price, 2)

    @computed_field
    @property
    def margin_pct(self) -> float | None:
        if self.purchase_price == 0:
            return None
        return round((self.profit / self.purchase_price) * 100, 2)

    class Config:
        from_attributes = True