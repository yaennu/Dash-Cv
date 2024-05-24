import dash
from dash import html
from dash import dcc

dash.register_page(__name__, path="/", name="Yannick")

layout = html.Div(
    children=[
        html.H1("Yannick Schwarz"),
        html.H3("Interactive CV Website"),
        html.Div(
            html.P([
                """This is the curriculum vitae website of Yannick Schwarz. 
                It is the attempt to visualise the CV in a more interactive way. \U0001F389"""
            ])
        ),
        html.H3("Technical Background of this Website"),
        html.Ul([
                html.Li("Data Preparation: Python"),
                html.Li([
                    "Version Control: Git (",
                    dcc.Link(
                        "GitHub repository",
                        href="https://github.com/yaennu/Dash-Cv",
                        target="_blank"
                    ),
                    ")"
                ]),
                html.Li("Testing: pytest"),
                html.Li("Database: Azure SQL Server"),
                html.Li("Frontend: Dash and Plotly (Python)"),
                html.Li("Containerization: Docker"),
                html.Li(
                    "CI/CD: GitHub Actions (every push builds and deploys a new Docker container)"),
                html.Li("Image Repository: GitHub Packages"),
                html.Li("Hosting: Azure Web App Service"),
                ]),
    ],
)
