import dash
import dash_bootstrap_components as dbc
from dash import html
from components import sidebar
from dotenv import load_dotenv
import os

load_dotenv()

app = dash.Dash(
    __name__,
    use_pages=True,
    external_stylesheets=[dbc.themes.BOOTSTRAP],
)

app.layout = html.Div(
    className="flex-container",
    children=[
        html.Div(
            className="flex-sidebar",
            children=[sidebar()],
        ),
        html.Div(
            className="flex-child",
            children=[dash.page_container],
        ),
    ],
)

if __name__ == "__main__":
    app.run_server(
        host=(
            os.getenv("APP_HOST_DOCKER")
            if os.getenv("RUN_LOCATION") == "Docker"
            else os.getenv("APP_HOST_LOCAL")
        ),
        port=os.getenv("APP_PORT"),
        debug=True,
    )
