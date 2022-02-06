import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
import Charts.charts as ch

dashboard =dbc.Card(
                    dbc.CardBody([
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
                                style={"width": "18rem"},
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
                                style={"width": "18rem"},
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
                                style={"width": "18rem"},
                                )
                            )
                        ]),
                        dbc.Row([
                            dbc.Col(ch.drawFigure2(),width=6),
                            dbc.Col(ch.drawFigure(),width=6)
                        ]
                        ,style={"margin":"10px"}
                        ),
                        dbc.Row(ch.drawFigure4()),
                    ])
                ,style={"height":"100%"}
                )