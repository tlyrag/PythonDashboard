import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
import Charts.charts as ch

dashboard =dbc.Card(
                    dbc.CardBody([
                        dbc.Row([
                            dbc.Col(html.H1('Valor 1'))
                            ,dbc.Col(html.H1('Valor 2'))
                            ,dbc.Col(html.H1('Valor 3'))
                        ]),
                        dbc.Row([
                            dbc.Col(ch.drawFigure()),
                            dbc.Col(ch.drawFigure())
                        ]),
                            dbc.Row(children=ch.drawFigure()),
                    ]
                    )
                )