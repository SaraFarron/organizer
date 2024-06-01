from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastui import FastUI, prebuilt_html

from src.charts.router import router as charts_router
from src.database import engine
from src.models import Base
from src.ui import home_page, page_wrapper

Base.metadata.create_all(bind=engine)
app = FastAPI()

app.include_router(charts_router, prefix="/api/charts", tags=["Charts"])


@app.get("/healthcheck")
async def healthcheck():
    """Health check."""
    return {"success": True}


@app.get("/api/", response_model=FastUI, response_model_exclude_none=True)
async def main_page():
    """Main page of the app."""
    return page_wrapper(home_page(), title="Title")


@app.get("/{path:path}")
async def html_landing():
    """Simple HTML page which serves the React app, comes last as it matches all paths."""
    return HTMLResponse(prebuilt_html(title="Title"))
