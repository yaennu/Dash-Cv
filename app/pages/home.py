import dash
from dash import dcc, html
import dash_bootstrap_components as dbc

dash.register_page(__name__, name="Home", path="/")


layout = dbc.Container(
    children=[
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.Img(
                            className="rounded-img",
                            src="/assets/ys.png",
                            width="100%",
                            style={"padding-left": "0"},
                        ),
                        html.P(
                            "Yannick Schwarz",
                            style={
                                "margin-top": "1.5rem",
                                "margin-bottom": "0rem",
                            },
                        ),
                        html.P(
                            "+41 79 810 25 04",
                            style={"margin-bottom": "0rem"},
                        ),
                        html.P(
                            dcc.Link(
                                "Mail me!",
                                href="mailto:yannick.schwarz@bluewin.ch",
                                target="_blank",
                            ),
                            style={"margin-bottom": "0rem"},
                        ),
                        html.P(
                            dcc.Link(
                                "LinkedIn",
                                href="https://www.linkedin.com/in/yannick-schwarz-313203159/",
                                target="_blank",
                            ),
                            style={"margin-bottom": "0rem"},
                        ),
                    ],
                    md=4,
                    style={"margin-bottom": "2rem"},
                ),
                dbc.Col(
                    [
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
                    Zürich.""",
                            ]
                        ),
                        html.P(
                            """As a data scientist, my main goal is to 
                            contextualise data and present key findings in an 
                            understandable and concise way using 
                            visualisations. In addition am also passionate 
                            about creating a simpler, more reproducible, more 
                            understandable and therefore more efficient working 
                            environment. As 
                            a strong believer in agile structures and lifelong 
                            learning, I am constantly educating myself, be it 
                            by searching for new packages or learning new 
                            technologies and languages."""
                        ),
                        html.P(
                            [
                                """With over five years of experience as 
                            a data scientist at """,
                                dcc.Link(
                                    "Gemeinsame Einrichtung KVG",
                                    href="https://www.kvg.org/ueber-uns/",
                                    target="_blank",
                                ),
                                """ (GE KVG), I have acquired a deep knowledge 
                            of data science methodologies, which I have 
                            successfully applied to numerous data analyses and 
                            projects (see below). My main focus was the 
                            calculation of """,
                                dcc.Link(
                                    "risk adjustment",
                                    href="https://www.kvg.org/versicherer/risikoausgleich/",
                                    target="_blank",
                                ),
                                """ in Swiss health
                          insurance and the validation of the data (about 100
                          million records per year). I led our two-person data 
                          science team, for three years.""",
                            ]
                        ),
                    ],
                    md=8,
                ),
            ]
        ),
        html.P(
            [
                """Now you can explore my website and find out more about me. 
                Above in the website header you can switch to my """,
                dcc.Link(
                    "CV",
                    href="/cv",
                ),
                """ in timeline and tabular form or explore the """,
                dcc.Link(
                    "skills",
                    href="/skills",
                ),
                """ I have 
            acquired throughout my education and career. For a more complete
            picture of my professional experience, you can download my CV with 
            the button below.""",
            ]
        ),
        html.Div(
            children=[
                dbc.Button(
                    "Download PDF CV (German)",
                    href="/static/Yannick-Schwarz-CV.pdf",
                    download="Yannick-Schwarz-CV.pdf",
                    external_link=True,
                    color="primary",
                    style={"margin-bottom": "2rem"},
                ),
            ],
            className="d-grid gap-2",
        ),
        html.H1("Projects"),
        html.Ul(
            children=[
                html.Li(
                    [
                        """Reports in R markdown: """,
                        html.Ul(
                            [
                                html.Li(
                                    [
                                        dcc.Link(
                                            "Annual report",
                                            href="https://www.kvg.org/wp-content/uploads/jahresbericht-2023-risikoausgleich.html",
                                            target="_blank",
                                        ),
                                        """ on the execution of risk 
                                            equalisation in health insurance 
                                            in Switzerland.""",
                                    ]
                                ),
                                html.Li(
                                    """Annual calculation of the lump 
                                            sum for a living donation in 
                                            Switzerland."""
                                ),
                            ]
                        ),
                    ]
                ),
                html.Li(
                    [
                        """Shiny Apps: """,
                        html.Ul(
                            [
                                html.Li(
                                    [
                                        dcc.Link(
                                            "Html table",
                                            href="https://gekvg.shinyapps.io/sl-check-tool/",
                                            target="_blank",
                                        ),
                                        """ (DT package) for searching monthly SL data.""",
                                    ]
                                ),
                                html.Li(
                                    """Employer reference creation (styled 
                                    word document) based on a excel 
                                    questionnaire (containerised with 
                                    docker)."""
                                ),
                            ]
                        ),
                    ]
                ),
                html.Li(
                    [
                        """R package: Calculation of risk equalisation in 
                        health insurance in Switzerland with test data
                        (""",
                        dcc.Link(
                            "zip-file",
                            href="https://www.kvg.org/wp-content/uploads/parallelberechnung.zip",
                            target="_blank",
                        ),
                        ").",
                    ]
                ),
                html.Li(
                    [
                        """AI chat bot: Development of a chat bot with a 
                        software provider to query the knowledge base of 
                        the company (ongoing)."""
                    ]
                ),
                html.Li(
                    [
                        """Dash App in Python: Call center dashboard 
                        (containerised with docker, ongoing)."""
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
                html.Li("Frontend: Dash, Bootstrap"),
                html.Li("Containerization: Docker"),
                html.Li(
                    "CI/CD: GitHub Actions (every push builds and deploys a new Docker container)"
                ),
                html.Li("Image Repository: GitHub Packages"),
                html.Li("Hosting: Azure Web App Service"),
                html.Li("Code Editor: VS Code"),
                html.Li("AI support: GitHub Copilot"),
            ]
        ),
    ],
)
