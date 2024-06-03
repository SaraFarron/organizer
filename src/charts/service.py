from plotly.offline import plot

from src.charts.config import X_COL, Y_COL
from src.charts.utils import charts_data


def income_chart():
    """Income chart."""
    return plot(charts_data("income", X_COL, Y_COL), output_type="div")


def expences_chart():
    """Expences chart."""
    return plot(charts_data("expences", X_COL, Y_COL), output_type="div")


def profits_chart():
    """Profits chart."""
    return plot(charts_data("profits", X_COL, Y_COL), output_type="div")
