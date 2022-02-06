# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

##### Importing Libs
from turtle import width
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd

##### Importing Folders
import Components.Header as header
import Components.Nav as nav
import Components.Dashboard as dashboard



external_stylesheets = [dbc.themes.DARKLY]
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
# =============================================================
# Layout
app.layout = html.Div(
        [
            dbc.Row(
                dbc.Col(
                    html.Div(dbc.Card(dbc.CardBody(header.header)))
                    ,width=12
                )
            ),
            dbc.Row(
                [
                    dbc.Col(
                        html.Div(
                            dbc.Card(
                                dbc.CardBody(nav.nav)
                                ,style={"height":"100vh"}
                            )
                        )
                        ,width=2
                    ),
                    dbc.Col(
                        html.Div(
                            [dashboard.dashboard]
                        )
                    ,width=10),
                ],
            ),
        ]
    ,style={"height":"100vh"}
    )



if __name__ == '__main__':
    app.run_server(debug=True)