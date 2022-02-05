# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

##### Importing Libs
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go

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
app.layout = dbc.Container([
    html.Div(
        [
            dbc.Row(
                dbc.Col(
                    html.Div(dbc.Card(dbc.CardBody(header.header)))
                    ,width=12
                )
            ),
            dbc.Row(
                [
                    dbc.Col(html.Div(dbc.Card(dbc.CardBody(nav.nav)))
                    ,width=2),
                    dbc.Col(html.Div([dashboard.dashboard]),width=10),
                ]
            ),
        ]
    )
])


if __name__ == '__main__':
    app.run_server(debug=True)