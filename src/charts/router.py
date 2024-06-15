from fastapi import APIRouter, Request
from fastui import FastUI
from fastui import components as c

from src.charts.config import PLOTS_HEIGHT
from src.charts.service import chart, expences_chart, income_chart, profits_chart
from src.ui import page_wrapper

router = APIRouter()


@router.get("/plot/income")
async def plot_income(request: Request):
    """Plot income chart."""
    return income_chart(request)


@router.get("/plot/expences")
async def plot_expences(request: Request):
    """Plot expences chart."""
    return expences_chart(request)


@router.get("/plot/profits")
async def plot_profits(request: Request):
    """Plot profits chart."""
    return profits_chart(request)


@router.get("/plot/{name}")
async def plot(request: Request, name: str):
    """Plot chart."""
    return chart(request, name)


@router.get("/income", response_model=FastUI, response_model_exclude_none=True)
async def income():
    """Income chart."""
    return page_wrapper(
        [c.Iframe(src="http://localhost:8000/api/charts/plot/income", width="100%", height=PLOTS_HEIGHT)],
    )


@router.get("/expences", response_model=FastUI, response_model_exclude_none=True)
async def expences():
    """Expences chart."""
    return page_wrapper(
        [c.Iframe(src="http://localhost:8000/api/charts/plot/expences", width="100%", height=PLOTS_HEIGHT)],
    )


@router.get("/profits", response_model=FastUI, response_model_exclude_none=True)
async def profits():
    """Profits chart."""
    return page_wrapper(
        [c.Iframe(src="http://localhost:8000/api/charts/plot/profits", width="100%", height=PLOTS_HEIGHT)],
    )
