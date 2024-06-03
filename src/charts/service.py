from fastapi import Request
from plotly.offline import plot

from src.charts.config import X_COL, Y_COL
from src.charts.utils import charts_data
from src.config import Templates


def income_chart(request: Request):
    """Income chart."""
    return Templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"plots": plot(charts_data("income", X_COL, Y_COL), output_type="div")},
    )


def expences_chart(request: Request):
    """Expences chart."""
    return Templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"plots": plot(charts_data("expences", X_COL, Y_COL), output_type="div")},
    )


def profits_chart(request: Request):
    """Profits chart."""
    return Templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"plots": plot(charts_data("profits", X_COL, Y_COL), output_type="div")},
    )
