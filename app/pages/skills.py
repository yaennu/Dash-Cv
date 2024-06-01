import dash
import pandas as pd
import plotly.graph_objects as go
import utils.DbData as db
from dash import Input, Output, callback, dcc, html
from py_plot_ge import plotly_ge as pg


dash.register_page(__name__, name="Skills")


layout = html.Div(
    className="flex-plot-with-radio",
    children=[
        html.Div(
            className="dash-graph",
            children=[
                dcc.Graph(id="SkillPlot"),
            ],
        ),
        html.Div(
            className="center-div",
            children=[
                html.Div(
                    children=[
                        html.H1("Skills:"),
                        dcc.RadioItems(
                            db.Skills.Skill.unique(),
                            "Technical",
                            id="Radio",
                        ),
                    ],
                ),
            ],
        ),
    ],
)


@callback(
    Output(component_id="SkillPlot", component_property="figure"),
    Input(component_id="Radio", component_property="value"),
)
def incoming_plot(Radio):

    polar_data = db.Skills[db.Skills["Skill"] == Radio]
    experience = polar_data[polar_data["Level"] == "Ist"].Value.reset_index(drop=True)
    r_experience = pd.concat(
        [
            experience,
            experience[
                [
                    0,
                ]
            ],
        ]
    )

    categories = pd.unique(polar_data.Bezeichnung)
    theta_cat = pd.concat(
        [
            pd.Series(categories),
            pd.Series(categories)[
                [
                    0,
                ]
            ],
        ]
    )

    fig = go.Figure()
    fig = fig.add_trace(
        go.Scatterpolar(
            r=r_experience,
            theta=theta_cat,
            fill="toself",
            name="Erfahrung",
            marker_color="#6c26ee",
        )
    )
    if Radio == "Technical":
        interest = polar_data[polar_data["Level"] == "Soll"].Value.reset_index(
            drop=True
        )
        r_interest = pd.concat(
            [
                interest,
                interest[
                    [
                        0,
                    ]
                ],
            ]
        )
        fig = fig.add_trace(
            go.Scatterpolar(
                r=r_interest,
                theta=theta_cat,
                name="Interesse",
                marker_color="#ff8000",
            )
        )
    pg.plotly_gelayout(
        fig,
        font_size=14,
    )
    fig = fig.update_layout(
        polar=dict(radialaxis=dict(visible=True, range=[0, 5])),
        height=400,
        width=550,
    )
    fig.update_traces(
        hovertemplate="%{theta}: %{r}",
    )

    return fig
