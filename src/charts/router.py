from fastapi import APIRouter
from fastui import FastUI
from fastui import components as c

from src.charts.service import expences_chart, income_chart, profits_chart
from src.ui import page_wrapper

router = APIRouter()


@router.get("/plot/income")
async def plot_income():
    """Plot income chart."""
    return income_chart()


@router.get("/plot/expences")
async def plot_expences():
    """Plot expences chart."""
    return expences_chart()


@router.get("/plot/profits")
async def plot_profits():
    """Plot profits chart."""
    return profits_chart()


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
