import dash
from dash import dcc, html, dash_table
import utils.DbData as db
import pandas as pd
import plotly.graph_objects as go
from py_plot_ge import plotly_ge as pg
import dash_bootstrap_components as dbc


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
    font_size=14,
)
fig.update_yaxes(showticklabels=False, showgrid=False, autorange="reversed")
fig.update_layout(
    height=300,
    margin=dict(l=0, r=0, b=0, t=0, pad=4),
)
fig.update_traces(hovertemplate="%{text}")

# Prepare data for table
table_data = db.Cv[["Thema", "Start", "Ende", "Ort", "Bezeichnung"]]

# Create the layout
layout = dbc.Container(
    children=[
        html.H1("Timeline"),
        html.P(
            [
                """This is my CV as a timeline with four different categories: 
                work, education, coding and diverse things which are related
                to my work. If you want to know more about a specific point, in 
                the timeline, just hover over the point or look up the details
                in the table below.""",
            ]
        ),
        dcc.Graph(id="CvPlot", figure=fig),
        # html.H1("Table"),
        # dash_table.DataTable(
        #    data=table_data.to_dict("records"),
        #    columns=[{"name": i, "id": i} for i in table_data],
        #    filter_action="native",
        #    sort_action="native",
        #    selected_columns=[],
        #    page_current=0,
        #    page_size=10,
        #    style_cell={"textAlign": "left"},
        # ),
    ],
)
