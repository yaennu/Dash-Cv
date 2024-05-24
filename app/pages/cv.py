import dash
import pandas as pd
import plotly.graph_objects as go
from py_plot_ge import plotly_ge as pg
import utils.DbData as db
from dash import Input, Output, callback, dcc, html, dash_table

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
        )
    )
pg.plotly_gelayout(
    fig,
    hovermode="x unified",
    plot_title="Lebenslauf",
)
fig.update_yaxes(showticklabels=False, showgrid=False, autorange="reversed")

# Prepare data for table
table_data = db.Cv[["Thema", "Start", "Ende", "Ort", "Bezeichnung"]]

layout = html.Div(
    children=[
        html.Div(
            html.Div(
                children=[
                    dcc.Graph(id="CvPlot", figure=fig),
                ],
            ),
            style={'margin-bottom': '33px'},
        ),

        html.Div(
            dash_table.DataTable(
                data=table_data.to_dict('records'),
                columns=[
                    {"name": i, "id": i} for i in table_data
                ],
                filter_action="native",
                sort_action="native",
                selected_columns=[],
                page_current=0,
                page_size=10,
            )
        )
    ]
)
