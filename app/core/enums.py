from sqlalchemy import Enum

item_status_enum = Enum(
    "listed",
    "unlisted",
    "sold",
    "being_delivered_to_warehouse",
    "delivered_to_warehouse",
    "being_delivered_to_client",
    "delivered_to_client",
    name="item_status"
)

location_level_enum = Enum(
    "warehouse",
    "room",
    "rack",
    "shelf",
    "slot",
    name="location_level"
)

org_plan_enum = Enum(
    "free",
    "pro",
    "enterprise",
    name="plan_type"
)

org_role_enum = Enum(
    "owner",
    "manager",
    "staff",
    name="role_type"
)

alert_status_enum = Enum(
    "pending",
    "read",
    "dismissed",
    name="alert_status"
)