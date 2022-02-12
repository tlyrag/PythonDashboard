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


def totalVotes():
    return  html.Div([
        dbc.Card(
            dbc.CardBody([
                dcc.Graph(
                    figure=px.bar(
                        df.df_total_votes, x="name", y="total_votes", color="name",
                        title="Total Votes per candidate",
                        labels ={"name":"Candidates","total_votes":"Total Votes", "name":""},
                        width=400,
                        height=400
                    ).update_layout(
                        title_x=0.2,
                        template='plotly_dark',
                        plot_bgcolor= 'rgba(0, 0, 0, 0)',
                        paper_bgcolor= 'rgba(0, 0, 0, 0)',
                        legend=dict(
                                orientation="h",
                                yanchor="bottom",
                                y=1.02,
                                xanchor="right",
                                x=1.02
                        ),
                    ),
                    config={
                        'displayModeBar': False
                        
                    }
                ) 
            ])
        ),  
    ])

def totalDistrict():
    return  html.Div([
        dbc.Card(
            dbc.CardBody([
                dcc.Graph(
                    figure=px.bar(
                        df.df_total_votes, x="name", y="total_winner_district", color="name",
                        title = "Total District Wins per candidate",
                        labels ={"name":"Candidates","total_winner_district":"District Wins", "name":""},
                        width=400,
                        height=400,
                    ).update_layout(
                        title_x=0.14,
                        template='plotly_dark',
                        plot_bgcolor= 'rgba(0, 0, 0, 0)',
                        paper_bgcolor= 'rgba(0, 0, 0, 0)',
                        legend=dict(
                            orientation="h",
                            yanchor="bottom",
                            y=1.02,
                            xanchor="right",
                            x=1.02
                        ),
                    ),
                    config={
                        'displayModeBar': False
                    }
                ) 
            ])
        ),  
    ])

def totalPercentage():
    return  html.Div([
        dbc.Card(
            dbc.CardBody([
                dcc.Graph(
                    figure=px.pie(
                        df.df_total_votes, names="name", values="total_percentage",color="name",
                        title = "Total Percentage per candidate",
                        width=380,
                        height=400,
                    ).update_layout(
                        template='plotly_dark',
                        plot_bgcolor= 'rgba(0, 0, 0, 0)',
                        paper_bgcolor= 'rgba(0, 0, 0, 0)',
                        title_x=0.15,
                        legend=dict(
                            
                            orientation="h",
                            yanchor="bottom",
                            y=1.02,
                            xanchor="right",
                            x=1.02
                        ),
                    ),
                    config={
                        'displayModeBar': False
                    }
                ) 
            ])
        ),  
    ])

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
                        mapbox_style="carto-positron", zoom=9.5,
                        labels={"winner":"Candidates"},
                        hover_data = {"Coderre_percentage": True, "Joly_percentage":True,"Bergeron_percentage":True},
                        color_continuous_scale="Redor",
                        opacity=0.7
                    ).update_layout(
                        template='plotly_dark',
                        plot_bgcolor= 'rgba(0, 0, 0, 0)',
                        paper_bgcolor= 'rgba(0, 0, 0, 0)',
                        mapbox_style="carto-darkmatter",
                        legend=dict(
                                yanchor="top",
                                y=0.5,
                                xanchor="right",
                                x=0.99
                        ),
                        autosize = True,
                        margin = dict(l=0,r=0,t=0,b=0)
                    )
                )
            ])
        ),  
    ])


#####################Iteractive Functions
