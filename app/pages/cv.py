import dash
from dash import dcc, html, Input, Output, callback
import utils.DbData as db
import pandas as pd
import plotly.graph_objects as go
from py_plot_ge import plotly_ge as pg
import dash_bootstrap_components as dbc
import dash_ag_grid as dag


dash.register_page(__name__, name="CV")

# Create the figure
fig = go.Figure()
for Category in pd.unique(db.Cv["Category"]):
    fig.add_trace(
        go.Scatter(
            x=db.Cv[db.Cv["Category"] == Category]["Start"],
            y=db.Cv[db.Cv["Category"] == Category]["Order"],
            mode="lines+markers",
            name=Category,
            text=db.Cv[db.Cv["Category"] == Category]["DescriptionShort"],
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
fig.update_xaxes(fixedrange=True)
fig.update_yaxes(fixedrange=True)


# Prepare data for table
table_data = db.Cv[["Category", "Start", "End", "Place", "Description"]]
col_names = table_data.columns
columnDefs = [
    {
        "field": col_name,
        "filter": True,
        # "autoHeight": True,
        "width": (
            500 if col_name == "Description" else 250 if col_name == "Place" else 150
        ),
        "cellStyle": {"white-space": "normal"},
    }
    for col_name in col_names
]

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
                in the table below or download my CV as pdf with the  
                button at the end of this page.""",
            ]
        ),
        dcc.Graph(id="CvPlot", figure=fig),
        html.H1("Table", style={"margin-top": "2rem"}),
        dag.AgGrid(
            id="getting-started-filter",
            rowData=table_data.to_dict("records"),
            columnDefs=columnDefs,
            style={
                "padding-bottom": "66px",
                "height": "500px",
            },
        ),
        html.Div(
            children=[
                dbc.Button(
                    "Download PDF CV",
                    href="/static/Yannick-Schwarz-CV.pdf",
                    download="Yannick-Schwarz-CV.pdf",
                    external_link=True,
                    color="primary",
                    style={"margin-bottom": "2rem"},
                ),
            ],
            className="d-grid gap-2",
        ),
    ],
)
