import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
import Charts.charts as ch
import dataframes.dataframe as df




dashboard = dbc.Container([
        dbc.Row([
            dbc.Col(                            
                    dbc.Card(
                    [
                        dbc.CardHeader("Most Voted",style = {}),
                        dbc.CardBody(
                            [
                                html.H4(id='card1', className="card-title, card text-info"),
                            ],
                        ),
                    ],
                    style={"width": "18rem","margin-left":"70px"},
                    )
                )
                ,dbc.Col(
                    dbc.Card(
                    [
                        dbc.CardHeader("Winner total Votes"),
                        dbc.CardBody(
                            [
                                html.H4(id='card2', className="card-title,card text-success"),
                            ],
                        ),
                    ],
                    style={"width": "18rem","margin-left":"50px"},
                    )
                )
                ,dbc.Col(
                    dbc.Card(
                    [
                        dbc.CardHeader("Winner Percentage"),
                        dbc.CardBody(
                            [
                                html.H4(id='card3', className="card-title, card text-danger"),
                            ]
                        ),
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

