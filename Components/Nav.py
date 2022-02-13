import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
from pandas import DataFrame
import dataframes.dataframe as df
import base64


user = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRWnW0NUpcrZcGZeUJ4e50ZLU8ugS9GPPoqww&usqp=CAU'

district_list = []

for district in df.df.district:
    district_list.append(district)

nav= [
    html.Div([
        dbc.Row(html.Img(src=user)),
        dbc.Row(html.H1('Jhon Doe')),
        dbc.Row(
            dbc.ListGroup([
                dbc.ListGroupItem(html.H5('Filter',style={"justify-align":"center"})),
                dbc.ListGroupItem(
                    dcc.Checklist(
                    )
                ),
                dcc.Dropdown(
                    options=[{"label":dist, "value":dist} for dist in district_list],
                    value = 'Select District',
                    id ='location',
                    style={'color':'black'},
                    placeholder='Select District'
                ),
                dbc.ListGroupItem('Logout'),
            ])
        )
    ]
    ,style={"justify-content": "space-between"}
    )
]


