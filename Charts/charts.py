##### Importing Libs
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import plotly.express as px
import plotly.graph_objects as go

##### Importing Dataframes
import dataframes.dataframe as df


def drawFigure():
    return  html.Div([
        dbc.Card(
            dbc.CardBody([
                dcc.Graph(
                    figure=px.bar(
                        df.df, x="district", y="total", color="winner"
                    ).update_layout(
                        template='plotly_dark',
                        plot_bgcolor= 'rgba(0, 0, 0, 0)',
                        paper_bgcolor= 'rgba(0, 0, 0, 0)',
                    ),
                    config={
                        'displayModeBar': False
                    }
                ) 
            ])
        ),  
    ])

def drawFigure2():
    return dcc.Graph(
    figure={
        'data': [
            {'x': df.df_top5.district , 'y': df.df_top5.Joly, 'type': 'bar', 'name': 'Joly'},
            {'x': df.df_top5.district , 'y': df.df_top5.Bergeron, 'type': 'bar', 'name': 'Bergeron'},
            {'x': df.df_top5.district , 'y': df.df_top5.Coderre, 'type': 'bar', 'name': 'Coderre'},
        ],
        'layout': {
            'title': 'Dash Data Visualization'
        }
    }
)