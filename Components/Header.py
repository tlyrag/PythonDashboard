import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

themes_list = [
    dbc.DropdownMenuItem('plotly_dark'),
    dbc.DropdownMenuItem('TBD1'),
    dbc.DropdownMenuItem('TBD2'),
    dbc.DropdownMenuItem('TBD3'),
    dbc.DropdownMenuItem('TBD4'),
]

def header(user):  
    return dbc.Row([
                    dbc.Col(html.Img(src='image'),width=1),
                    dbc.Col(
                        html.H4(f'Hello {user}, Welcome to the Python Dashboard'),
                        width=9
                        ),
                    dbc.Col(
                        dbc.DropdownMenu(
                            label='Choose Theme',id="themes",children=themes_list, direction="start"
                        ),
                        width=2
                    )
                ])
     