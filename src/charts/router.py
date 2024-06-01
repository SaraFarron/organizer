from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from fastui import FastUI, prebuilt_html

from src.ui import home_page, page_wrapper

router = APIRouter()


@router.get("/healthcheck")
async def healthcheck():
    """Health check."""
    return {"success": True}


@router.get("/api/", response_model=FastUI, response_model_exclude_none=True)
async def main_page():
    """Main page of the app."""
    return page_wrapper(home_page(), title="Title")


@router.get("/{path:path}")
async def html_landing():
    """Simple HTML page which serves the React app, comes last as it matches all paths."""
    return HTMLResponse(prebuilt_html(title="Title"))
