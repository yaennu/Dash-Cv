import dash
import pandas as pd
import plotly.graph_objects as go
import utils.DbData as db
from dash import Input, Output, callback, dcc, html

dash.register_page(__name__, name="Skills")


layout = html.Div(
    className="flex-container",
    children=[
        html.Div(
            className="flex-child",
            children=[
                html.Div(
                    className="selector-box",
                    children=[
                        html.H4("Skills:"),
                        dcc.RadioItems(
                            ["Technical", "Social", "Methodical"],
                            "Technical",
                            id="Radio",
                        ),
                    ],
                ),
            ],
        ),
        html.Div(
            className="flex-child",
            children=[
                dcc.Graph(id="SkillPlot"),
            ],
        ),
    ],
)


@callback(
    Output(component_id="SkillPlot", component_property="figure"),
    Input(component_id="Radio", component_property="value"),
)
def incoming_plot(Radio):
    if Radio == "Technical":
        polar_data = db.Skills[db.Skills["Skill"] == "Technical"]
    elif Radio == "Social":
        polar_data = db.Skills[db.Skills["Skill"] == "Social"]
    elif Radio == "Methodical":
        polar_data = db.Skills[db.Skills["Skill"] == "Methodical"]
    Categories = pd.unique(polar_data.Bezeichnung)
    fig = go.Figure()
    fig = fig.add_trace(
        go.Scatterpolar(
            r=polar_data[polar_data["Level"] == "Soll"].Value,
            theta=Categories,
            fill="toself",
            name="Interesse",
        )
    )
    fig = fig.add_trace(
        go.Scatterpolar(
            r=polar_data[polar_data["Level"] == "Ist"].Value,
            theta=Categories,
            fill="toself",
            name="Erfahrung",
        )
    )
    fig = fig.update_layout(
        polar=dict(radialaxis=dict(visible=True, range=[0, 5])),
        showlegend=False,
    )

    return fig
