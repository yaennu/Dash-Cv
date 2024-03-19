import dash
import pandas as pd
import plotly.graph_objects as go
import utils.DbData as db
from dash import Input, Output, callback, dcc, html

dash.register_page(__name__, name="Interessen")


layout = html.Div(
    className="flex-container",
    children=[
        html.Div(
            className="flex-child",
            children=[
                html.Div(
                    className="selector-box",
                    children=[
                        html.H4("Auswahl:"),
                        dcc.Dropdown(
                            ["Cv", "Interests"],
                            "Interests",
                            id="Dropdown",
                        ),
                    ],
                ),
            ],
        ),
        html.Div(
            className="flex-child",
            children=[
                dcc.Graph(id="IntPlot"),
                html.H5("""Bemerkung"""),
            ],
        ),
    ],
)


@callback(
    Output(component_id="IntPlot", component_property="figure"),
    Input(component_id="Dropdown", component_property="value"),
)
def incoming_plot(Dropdown):
    Dropdown = "Interests"
    Categories = pd.unique(db.Interests.Bezeichnung)
    fig = go.Figure()
    fig = fig.add_trace(
        go.Scatterpolar(
            r=db.Interests[db.Interests["Thema"] == "Interesse"].Wert,
            theta=Categories,
            fill="toself",
            name="Interesse",
        )
    )
    fig = fig.add_trace(
        go.Scatterpolar(
            r=db.Interests[db.Interests["Thema"] == "Erfahrung"].Wert,
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
