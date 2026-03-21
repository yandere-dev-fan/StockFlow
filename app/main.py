from fastapi import FastAPI, APIRouter
from starlette.middleware.cors import CORSMiddleware
from app.modules.users.models import User
from app.modules.organizations.models import Organization, OrgMember
from app.modules.items.models import Item, ItemType, ItemUnit
from app.modules.alerts.models import Alert, AlertRule
from app.modules.locations.models import Location
from app.modules.sales.models import Sale
from app.modules.organizations import service
from app.modules.organizations.router import router as organizations_router
# from app.modules.users.router import router as users_router
# from app.modules.alerts.router import router as alerts_router
# from app.modules.items import router as items_router
from app.modules.locations.router import router as locations_router
# from app.modules.sales import router as sales_router

app = FastAPI(title="StockFlow", version="1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
)


app.include_router(locations_router)
app.include_router(organizations_router)
# app.include_router(users_router)
# app.include_router(items_router)
# app.include_router(alerts_router)
# app.include.router(sales_router)


