import dash
from dash import dcc, html, dash_table
import utils.DbData as db
import pandas as pd
import plotly.graph_objects as go
from py_plot_ge import plotly_ge as pg


dash.register_page(__name__, name="CV")

# Create the figure
fig = go.Figure()
for Thema in pd.unique(db.Cv["Thema"]):
    fig.add_trace(
        go.Scatter(
            x=db.Cv[db.Cv["Thema"] == Thema]["Start"],
            y=db.Cv[db.Cv["Thema"] == Thema]["ThemaWert"],
            mode="lines+markers",
            name=Thema,
            text=db.Cv[db.Cv["Thema"] == Thema]["Bezeichnung"],
            line=dict(width=5),
            marker=dict(size=13),
        )
    )
pg.plotly_gelayout(
    fig,
    hovermode="x unified",
)
fig.update_yaxes(showticklabels=False, showgrid=False, autorange="reversed")

# Prepare data for table
table_data = db.Cv[["Thema", "Start", "Ende", "Ort", "Bezeichnung"]]

# Create the layout
layout = html.Div(
    children=[
        html.Div(
            className="whole-page-div",
            children=[
                html.H3("Timeline"),
                dcc.Graph(id="CvPlot", figure=fig),
            ],
        ),
        html.Div(
            className="whole-page-div",
            children=[
                html.H3("Table"),
                dash_table.DataTable(
                    data=table_data.to_dict("records"),
                    columns=[{"name": i, "id": i} for i in table_data],
                    filter_action="native",
                    sort_action="native",
                    selected_columns=[],
                    page_current=0,
                    page_size=10,
                    style_cell={"textAlign": "left"},
                ),
            ],
        ),
    ],
)
