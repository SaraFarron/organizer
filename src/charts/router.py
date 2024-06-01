from fastapi import APIRouter
from fastui import FastUI
from fastui import components as c

from src.ui import page_wrapper

router = APIRouter()


@router.get("/income", response_model=FastUI, response_model_exclude_none=True)
async def income():
    """Income chart."""
    return page_wrapper([c.Iframe(src="https://pydantic.dev", width="100%", height=400)])


@router.get("/expences", response_model=FastUI, response_model_exclude_none=True)
async def expences():
    """Expences chart."""
    return page_wrapper([c.Iframe(src="https://pydantic.dev", width="100%", height=400)])


@router.get("/profits", response_model=FastUI, response_model_exclude_none=True)
async def profits():
    """Profits chart."""
    return page_wrapper([c.Iframe(src="https://pydantic.dev", width="100%", height=400)])
