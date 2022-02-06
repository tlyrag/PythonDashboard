import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import dataframes.dataframe as data

nav= [
    html.Div([
        dbc.Row(html.H1('Username'),style={"height":"200px"}),
        dbc.Row(
            dbc.ListGroup([
                dbc.ListGroupItem(html.H5('Filter',style={"justify-align":"center"})),
                dbc.ListGroupItem(
                    dcc.Checklist(
                        data.df.columns
                    )
                ),
                dbc.ListGroupItem('News'),
                dbc.ListGroupItem('Logout'),
            ])
        )
    ]
    ,style={"justify-content": "space-between"}
    )
]