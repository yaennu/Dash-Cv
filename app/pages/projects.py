import dash
from dash import html
from dash import dcc

dash.register_page(__name__, name="Projects")

layout = html.Div(
    children=[
        html.H1("Existing Projects"),
        html.Ul([
            html.Li([
                dcc.Link(
                    "Annual report",
                    href="https://www.kvg.org/wp-content/uploads/jahresbericht-2023-risikoausgleich.html",
                    target="_blank"
                ),
                """ in R markdown: on the execution of risk equalisation in 
                health insurance in Switzerland.""",
            ]),
            html.Li([
                dcc.Link(
                    "RA calculation",
                    href="https://www.kvg.org/wp-content/uploads/parallelberechnung.zip",
                    target="_blank"
                ),
                """ in R: zip-file of the calculation of risk equalisation in 
                health insurance in Switzerland.""",
            ]),
            html.Li([
                dcc.Link(
                    "Shiny App",
                    href="https://gekvg.shinyapps.io/sl-check-tool/",
                    target="_blank"
                ),
                """ in R: html table (DT package) for searching monthly SL data.""",
            ]),
            html.Li([
                """Shiny App in R: employer reference creation 
                (styled word document) based on a excel questionnaire 
                (containerised with docker)."""
            ]),
            html.Li([
                """Dash App in Python: call center dashboard (containerised with docker)."""
            ]),
            html.Li([
                """Annual report in R markdown: Annual calculation of the lump 
                sum for a living donation in Switzerland."""
            ]),
        ]),
    ],
)
