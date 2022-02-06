import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
import Charts.charts as ch

dashboard = dbc.Container([
                        dbc.Row([
                            dbc.Col(                            
                                dbc.Card(
                                [
                                    dbc.CardHeader("This is the header"),
                                    dbc.CardBody(
                                        [
                                            html.H4("Card title", className="card-title"),
                                            html.P("This is some card text", className="card-text"),
                                        ]
                                    ),
                                    dbc.CardFooter("This is the footer"),
                                ],
                                style={"width": "18rem","margin-left":"70px"},
                                )
                            )
                            ,dbc.Col(
                                dbc.Card(
                                [
                                    dbc.CardHeader("This is the header"),
                                    dbc.CardBody(
                                        [
                                            html.H4("Card title", className="card-title"),
                                            html.P("This is some card text", className="card-text"),
                                        ]
                                    ),
                                    dbc.CardFooter("This is the footer"),
                                ],
                                style={"width": "18rem","margin-left":"50px"},
                                )
                            )
                            ,dbc.Col(
                                dbc.Card(
                                [
                                    dbc.CardHeader("This is the header"),
                                    dbc.CardBody(
                                        [
                                            html.H4("Card title", className="card-title"),
                                            html.P("This is some card text", className="card-text"),
                                        ]
                                    ),
                                    dbc.CardFooter("This is the footer"),
                                ],
                                style={"width": "18rem","margin-left":"50px"},
                                )
                            )
                        ]),
                        dbc.Row([
                            dbc.Col(ch.totalPercentage(),width=4),
                            dbc.Col(ch.totalVotes(),width=4),
                            dbc.Col(ch.totalDistrict(),width=4),
                        ]
                        ,style={"margin":"10px"}
                        ),
                        dbc.Row(ch.drawFigure4()),
                    ])
