# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

##### Importing Libs
from turtle import width
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import time


##### Importing Folders
import Components.Header as header
import Components.Nav as nav
import Components.Dashboard as dashboard
import dataframes.dataframe as df
import Charts.charts as ch



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
                    html.Div(dbc.Card(dbc.CardBody(
                        header.header
                    )))
                    ,width=12,style={"margin-bottom":"10px"}
                )
            ),
            dbc.Row(
                [
                    dbc.Col(
                        html.Div(
                            dbc.Card(
                                dbc.CardBody(
                                    nav.nav
                                    )
                                ,style={"height":"100vh"}
                            )
                        )
                        ,width=2
                    ),
                    dbc.Col(
                        html.Div(
                            [
                                dashboard.dashboard,
                                dcc.Input(id='my-input', value='initial value', type='text'),
                                html.Div(id='my-output'),
                            ]
                        )
                    ,width=10),
                ],
            ),
        ]
    ,style={"height":"100vh"}
    
    )

@app.callback(
    [
        Output(component_id='card1', component_property='children'),
        Output(component_id='card2', component_property='children'),
        Output(component_id='card3', component_property='children'),
        Output(component_id='vote_chart',component_property='figure'),
        Output(component_id='percentage_chart',component_property='figure')
    ],
    [
        Input(component_id='location', component_property='value')
    ]
)
def update_output_div(input_value):
    if input_value == 'Select District':
        time.sleep(0.1)
        return (
            "Winner : " + str(df.df_total_votes['name'][1]),
            "Votes : " + str(df.df_total_votes['total_votes'][1]),
            "Percentage : " + str(df.df_total_votes['total_percentage'][1]),
            ch.total_votes_chart,
            ch.total_percentage_chart

            
        )
    else:
        time.sleep(0.1)
        return (
            "Winner : " + df.df[df.df['district'] == input_value].winner
            ,"Votes : " + df.df[df.df['district'] == input_value].winner_votes
            ,"Percentage : " + df.df[df.df['district'] == input_value].winner_percentage
            ,ch.update_district_votes_chart(input_value)
            ,ch.update_district_percentage_chart(input_value)
  
        )

if __name__ == '__main__':
    app.run_server(debug=True)