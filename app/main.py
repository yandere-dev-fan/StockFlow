from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from app.modules.users.models import User
from app.modules.organizations.models import Organization, OrgMember
from app.modules.items.models import Item, ItemType, ItemUnit
from app.modules.alerts.models import Alert, AlertRule
from app.modules.locations.models import Location
from app.modules.sales.models import Sale

app = FastAPI(title="StockFlow", version="1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
)

# app.include_router(organizations_router)
# app.include_router(users_router)
# app.include_router(locations_router)
# app.include_router(items_router)
# app.include_router(alerts_router)

@app.get("/")
def root():
    return {"status": "ok"}
