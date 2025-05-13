from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount(
    "/static", StaticFiles(directory="src/stellar_harvest_ie_ui/static"), name="static"
)
templates = Jinja2Templates(directory="src/stellar_harvest_ie_ui/templates")

from .routers import users, dashboard, realtime

# app.include_router(users.router, prefix="/auth", tags=["users"])
# app.include_router(realtime.router, prefix="/ws", tags=["realtime"])
app.include_router(dashboard.router, prefix="", tags=["dashboard"])
