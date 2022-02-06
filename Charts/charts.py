##### Importing Libs
import dash
from dash import dcc
from dash import html
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
                        df.df, x="district", y="winner_percentage", color="winner"
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

def drawFigure3():
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

#def drawFigure4():
 #   return px.choropleth_mapbox(df.df, locations = 'district_id', geojson=df.df2, color='total', color_continuous_scale='Redor',hover_data={'total': True})


def drawFigure4():
    return  html.Div([
        dbc.Card(
            dbc.CardBody([
                dcc.Graph(figure=
                    px.choropleth_mapbox(df.df, geojson=df.df2, color="winner",
                        locations="district_id",
                        center={"lat": 45.5517, "lon": -73.7073},
                        mapbox_style="carto-positron", zoom=9,
                        hover_data = {"Coderre_percentage": True, "Joly_percentage":True,"Bergeron_percentage":True}
                    ).update_layout(        
                        template='plotly_dark',
                        plot_bgcolor= 'rgba(0, 0, 0, 0)',
                        paper_bgcolor= 'rgba(0, 0, 0, 0)',)
                )
            ])
        ),  
    ])
