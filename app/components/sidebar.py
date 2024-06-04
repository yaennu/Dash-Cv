import dash
import dash_bootstrap_components as dbc
from dash import html
from dash import dcc


def sidebar():
    return html.Div(
        children=[
            dbc.Nav(
                [
                    dbc.NavLink(
                        children=[
                            html.Div(page["name"], className="ms-2"),
                        ],
                        href=page["path"],
                        active="exact",
                    )
                    for page in dash.page_registry.values()
                ],
                vertical=True,
                pills=True,
            ),
            html.Div(
                className="contact",
                children=["Yannick Schwarz"],
                style={"margin-top": "2rem"},
            ),
            html.Div(
                className="contact",
                children=["+41 79 810 25 04"],
            ),
            html.Div(
                className="contact",
                children=[
                    dcc.Link(
                        "Mail me!",
                        href="mailto:yannick.schwarz@bluewin.ch",
                        target="_blank",
                    )
                ],
            ),
            html.Div(
                className="contact",
                children=[
                    dcc.Link(
                        "LinkedIn",
                        href="https://www.linkedin.com/in/yannick-schwarz-313203159",
                        target="_blank",
                    )
                ],
            ),
            # html.Div(
            #    className="portrait-container",
            #    children=[
            #        html.Img(
            #            className="rounded-img",
            #            src="assets/ys.jpeg",
            #            width="220px",
            #        ),
            #    ],
            # ),
        ],
    )
