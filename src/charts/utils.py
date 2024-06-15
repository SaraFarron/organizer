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


def get_dataframe(data: dict, key: str, dt_fmt: str = "%d.%m.%Y %H:%M:%S"):
    """Get dataframe from tmp.json."""
    rows = [adapt_columns(item) for item in data if item["model"] == "charts." + key]
    dataframe = pd.DataFrame(rows)
    try:
        dataframe[Y_COL] = dataframe[Y_COL].str.replace(",", ".").astype(float).abs()
    except AttributeError:
        dataframe[Y_COL] = dataframe[Y_COL].astype(float).abs()
    dataframe[X_COL] = pd.to_datetime(dataframe[X_COL], format=dt_fmt)
    return dataframe


def get_plot_data(
    data: pd.DataFrame,
    x_col: str = "Date",
    y_col: str = "Total",
    after: str = "2021-01-01",
):
    """Retreives data from table and adapts for plots."""
    xy_data = data[[x_col, y_col]]

    sliced_data = xy_data.loc[xy_data[x_col] > after]

    unsorted = sliced_data.groupby(sliced_data[x_col].dt.strftime("%Y-%m"))[y_col].sum().reset_index()
    return unsorted.sort_values(by=x_col)


def charts_data(kind: Literal["income", "expences", "profits"], x_column: str, y_column: str):
    """Get charts data."""
    data = load_tmp_data()
    if kind == "profits":
        table = get_dataframe(data, "income", dt_fmt="%Y-%m-%d")
        expences = get_dataframe(data, "expences", dt_fmt="%Y-%m-%d")
        table[Y_COL] = table[Y_COL] - expences[Y_COL]
    else:
        table = get_dataframe(data, kind, dt_fmt="%Y-%m-%d")
    if x_column not in table.columns or y_column not in table.columns:
        raise HTTPException(
            status_code=404,
            detail=f"Column not found: {x_column} or {y_column} not in {table.columns}",
        )
    plot_data = get_plot_data(table, x_col=x_column, y_col=y_column)
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


def common_chart(name: str, x_column: str, y_column: str, kind: Literal["bar", "line"]):
    """Get common chart."""
