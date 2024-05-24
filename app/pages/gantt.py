import dash
import pandas as pd
import plotly.graph_objects as go
from py_plot_ge import plotly_ge as pg
import utils.DbData as db
from dash import Input, Output, callback, dcc, html, dash_table

dash.register_page(__name__, name="Zeitstrahl")


layout = html.Div(
    children=[
        html.Div(
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
                                    "Cv",
                                    id="Dropdown",
                                ),
                            ],
                        ),
                    ],
                ),
                html.Div(
                    className="flex-child",
                    children=[
                        dcc.Graph(id="GanttPlot"),
                        html.H5("""Bemerkung"""),
                    ],
                ),
            ],
        ),
    ]
)


@callback(
    Output(component_id="GanttPlot", component_property="figure"),
    Input(component_id="Dropdown", component_property="value"),
)
def incoming_plot(Dropdown):
    if Dropdown == "Cv":
        fig = go.Figure()
        for Thema in pd.unique(db.Cv["Thema"]):
            fig.add_trace(
                go.Scatter(
                    x=db.Cv[db.Cv["Thema"] == Thema]["Start"],
                    y=db.Cv[db.Cv["Thema"] == Thema]["Wert"],
                    mode="lines+markers",
                    name=Thema,
                    text=db.Cv[db.Cv["Thema"] == Thema]["Bezeichnung"],
                )
            )
            fig.update_traces(
                hovertemplate="Ab %{x}<br>%{text}<extra></extra>")

        # GE layout for plot
        pg.plotly_gelayout(
            fig,
            hovermode="closest",
            yaxis_title="Wert",
            plot_title="Lebenslauf",
        )

    return fig
