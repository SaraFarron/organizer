import json
from typing import Literal

import pandas as pd
import plotly.graph_objs as go
from fastapi import HTTPException
from plotly.subplots import make_subplots

from src.charts.config import X_COL, Y_COL


def load_tmp_data() -> dict:
    """Loads data from tmp.json."""
    with open("tmp.json") as f:
        return json.load(f)


def adapt_columns(row: dict):
    """Adapt columns from tmp.json."""
    return {
        X_COL: row["fields"]["month"],
        Y_COL: row["fields"]["total"],
    }


def get_dataframe(data: dict, key: str):
    """Get dataframe from tmp.json."""
    rows = [adapt_columns(item) for item in data if item["model"] == "charts." + key]
    return pd.DataFrame(rows)


def get_plot_data(
    data: pd.DataFrame,
    dt_fmt: str = "%d.%m.%Y %H:%M:%S",
    x_col: str = "Date",
    y_col: str = "Total",
    after: str = "2021-01-01",
):
    """Retreives data from table and adapts for plots."""
    xy_data = data[[x_col, y_col]]

    try:
        xy_data[y_col] = xy_data[y_col].str.replace(",", ".").astype(float).abs()
    except AttributeError:
        xy_data[y_col] = xy_data[y_col].astype(float).abs()
    xy_data[x_col] = pd.to_datetime(xy_data[x_col], format=dt_fmt)

    sliced_data = xy_data.loc[xy_data[x_col] > after]

    unsorted = sliced_data.groupby(sliced_data[x_col].dt.strftime("%Y-%m"))[y_col].sum().reset_index()
    return unsorted.sort_values(by=x_col)


def charts_data(kind: Literal["income", "expences", "profits"], x_column: str, y_column: str):
    """Get charts data."""
    data = load_tmp_data()
    table = get_dataframe(data, kind)
    if x_column not in table.columns or y_column not in table.columns:
        raise HTTPException(
            status_code=404,
            detail=f"Column not found: {x_column} or {y_column} not in {table.columns}",
        )
    plot_data = get_plot_data(table, x_col=x_column, y_col=y_column, dt_fmt="%Y-%m-%d")
    layout = go.Layout(yaxis={"tickformat": "~s"})
    fig = make_subplots()
    fig.add_scatter(
        x=plot_data[x_column],
        y=plot_data[y_column],
        line_shape="spline",
        name=kind,
    )
    fig.update_layout(layout)
    return fig
