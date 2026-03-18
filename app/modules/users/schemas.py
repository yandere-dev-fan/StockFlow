from datetime import datetime
from uuid import UUID
from pydantic import BaseModel, EmailStr


class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str


class UserUpdate(BaseModel):
    name: str | None = None
    email: EmailStr | None = None
    password: str | None = None


class UserResponse(BaseModel):
    id: UUID
    name: str
    email: EmailStr
    created_at: datetime

    class Config:
        from_attributes = True