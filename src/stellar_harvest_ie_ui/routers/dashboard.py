from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse

router = APIRouter()


@router.get("/", response_class=HTMLResponse)
async def dashboard(request: Request):
    return """
    <html>
        <head><title>Dashboard | Stellar Harvest</title></head>
        <body>
            <h1>Welcom to your Dashboard</h1>
            <p>Metrics and charts will go here.</p>
        </body>
    </html>
    """
