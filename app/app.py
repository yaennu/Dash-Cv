import dash
import dash_bootstrap_components as dbc
from dotenv import load_dotenv
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
    ],
    sticky="top",
)

app.layout = dbc.Container(
    children=[nav, dash.page_container],
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
