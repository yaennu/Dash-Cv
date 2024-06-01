import dash
from dash import dcc, html

dash.register_page(__name__, name="Home", path="/")


layout = html.Div(
    children=[
        html.H1("About Me"),
        html.P(
            [
                """Hello and welcome to my website. My name is Yannick 
                    Schwarz. I was born and raised in """,
                dcc.Link(
                    "Bern",
                    href="https://www.bscyb.ch/",
                    target="_blank",
                ),
                """, but now live in 
                    Zürich. I am passionate about many things, but especially 
                    about data. First I like to dive deep into the data, but 
                    then my goal is to get a direct benefit from the data. I 
                    focus on visualising the benefits of the data in a simple 
                    and straightforward way.""",
            ]
        ),
        html.P(
            [
                """I studied economics and was introduced to data and the 
                    programming language R during my master studies at the
                      University of Bern. After my Masters I worked for five 
                      years at the """,
                dcc.Link(
                    "Gemeinsame Einrichtung KVG",
                    href="https://www.kvg.org/",
                    target="_blank",
                ),
                """. My main focus was the calculation of """,
                dcc.Link(
                    "risk adjustment",
                    href="https://www.kvg.org/versicherer/risikoausgleich/",
                    target="_blank",
                ),
                """ in Swiss health 
                      insurance and the validation of the data (about 100 
                      million records per year). Besides the main focus, 
                      various small and large side projects (see below) were 
                      tackled by our two-person data science team, which 
                      I led for three years.""",
            ]
        ),
        html.P(
            [
                """Now you can explore my website and find out more about me. On 
            the left you will find the website menu where you can switch to 
            my """,
                dcc.Link(
                    "CV",
                    href="/cv",
                ),
                """ in timeline or tabular form and explore the """,
                dcc.Link(
                    "skills",
                    href="/skills",
                ),
                """ I have 
            acquired throughout my education and career.""",
            ]
        ),
        html.H1("Projects"),
        html.Ul(
            children=[
                html.Li(
                    [
                        """AI chat bot: develop a chat bot with a software 
                        provider to query the knowledge base of the company."""
                    ]
                ),
                html.Li(
                    [
                        dcc.Link(
                            "Annual report",
                            href="https://www.kvg.org/wp-content/uploads/jahresbericht-2023-risikoausgleich.html",
                            target="_blank",
                        ),
                        """ in R markdown: on the execution of risk 
                        equalisation in health insurance in Switzerland.""",
                    ]
                ),
                html.Li(
                    [
                        dcc.Link(
                            "RA calculation",
                            href="https://www.kvg.org/wp-content/uploads/parallelberechnung.zip",
                            target="_blank",
                        ),
                        """ in R: zip-file of the calculation of risk equalisation in 
                health insurance in Switzerland.""",
                    ]
                ),
                html.Li(
                    [
                        dcc.Link(
                            "Shiny App",
                            href="https://gekvg.shinyapps.io/sl-check-tool/",
                            target="_blank",
                        ),
                        """ in R: html table (DT package) for searching monthly SL data.""",
                    ]
                ),
                html.Li(
                    [
                        """Shiny App in R: employer reference creation 
                (styled word document) based on a excel questionnaire 
                (containerised with docker)."""
                    ]
                ),
                html.Li(
                    [
                        """Dash App in Python: call center dashboard 
                        (containerised with docker)."""
                    ]
                ),
                html.Li(
                    [
                        """Annual report in R markdown: Annual calculation of the lump 
                sum for a living donation in Switzerland."""
                    ]
                ),
            ]
        ),
        html.H1("Technical Background of this Website"),
        html.Ul(
            [
                html.Li("Data Preparation: Python"),
                html.Li(
                    [
                        "Version Control: Git (",
                        dcc.Link(
                            "GitHub repository",
                            href="https://github.com/yaennu/Dash-Cv",
                            target="_blank",
                        ),
                        ")",
                    ]
                ),
                html.Li("Testing: pytest"),
                html.Li("Database: Azure SQL Server"),
                html.Li("Frontend: Dash and Plotly (Python)"),
                html.Li("Containerization: Docker"),
                html.Li(
                    "CI/CD: GitHub Actions (every push builds and deploys a new Docker container)"
                ),
                html.Li("Image Repository: GitHub Packages"),
                html.Li("Hosting: Azure Web App Service"),
                html.Li("Code Editor: VS Code"),
            ]
        ),
    ],
)
