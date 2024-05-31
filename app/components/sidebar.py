import dash
import dash_bootstrap_components as dbc
from dash import html
from dash import dcc


def sidebar():
    return html.Div(
        children=[
            html.Div(
                className="contact",
                children=["YANNICK SCHWARZ"],
                style={"margin-top": "0px"},
            ),
            html.Div(
                className="contact",
                children=["+41 79 810 25 04"],
                style={"margin-top": "0px"},
            ),
            html.Div(
                className="contact",
                children=[
                    dcc.Link(
                        "yannick.schwarz@bluewin.ch",
                        href="mailto:yannick.schwarz@bluewin.ch",
                        target="_blank",
                    )
                ],
                style={"margin-bottom": "50px"},
            ),
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
            # dbc.Button(
            #    "LinkedIn",
            #    href="https://www.linkedin.com/in/yannick-schwarz-313203159/",
            #    target="_blank",
            # ),
        ],
    )
