import dash
from dash import html

dash.register_page(__name__, path="/", name="Yannick")

layout = html.Div(
    className="flex-container",
    children=[
        html.Div(
            """This is the Curriculum Vitae website of Yannick Schwarz. 
            It is the attempt to visualise the CV in a more interactive way. 
            The values shown in the graphs should not be taken too seriously."""
        ),
    ],
)
