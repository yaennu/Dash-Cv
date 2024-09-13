import dash
import dash_bootstrap_components as dbc
from dotenv import load_dotenv
from dash import dcc, html

import os

load_dotenv()

app = dash.Dash(
    __name__,
    use_pages=True,
    external_stylesheets=[dbc.themes.BOOTSTRAP],
)

nav = dbc.Navbar(
    children=[
        dbc.NavItem(dbc.NavLink("Home", href="/")),
        dbc.NavItem(dbc.NavLink("CV", href="/cv")),
        dbc.NavItem(dbc.NavLink("Skills", href="/skills")),
        dbc.NavItem(
            dbc.NavLink(
                "Assistant",
                href="/assistant",
                style={"color": "red"},
            ),
        ),
    ],
    sticky="top",
)

footer = html.Div(
    children=[
        html.Div(
            dcc.Link(
                "LinkedIn",
                href="https://www.linkedin.com/in/yannick-schwarz-313203159/",
                target="_blank",
            )
        ),
        html.Div("+41 79 810 25 04"),
        html.Div(
            dcc.Link(
                "yannick.schwarz@bluewin.ch",
                href="mailto:yannick.schwarz@bluewin.ch",
                target="_blank",
            )
        ),
    ],
    className="footer-style",
)

app.layout = dbc.Container(
    children=[nav, dash.page_container, footer],
    fluid=True,
)

if __name__ == "__main__":
    app.run_server(
        host=(
            os.getenv("APP_HOST_DOCKER")
            if os.getenv("RUN_LOCATION") == "Docker"
            else os.getenv("APP_HOST_LOCAL")
        ),
        port=os.getenv("APP_PORT"),
        debug=(False if os.getenv("RUN_LOCATION") == "Docker" else True),
    )
