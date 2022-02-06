from encodings import CodecRegistryError
import plotly.express as px
import pandas as pd
import numpy as np
import json

################################ Working with data election ###################################
df = px.data.election()
df_top5 = df.head()

## Possible Columns winner_percentage, winner_votes, candidate_percentage, 
## Adding Columns to dataframe
df['Coderre_percentage'] = round(df.Coderre/df.total,2)
df['Bergeron_percentage'] = round(df.Bergeron/df.total,2)
df['Joly_percentage'] = round(df.Joly/df.total,2)

df['winner_votes'] = np.where((df.winner =='Coderre'), df.Coderre, 
                     np.where((df.winner == 'Bergeron'), df.Bergeron, 
                     np.where((df.winner == 'Joly'), df.Joly, 
                     'No Change')))

df['winner_percentage'] =   np.where((df.winner =='Coderre'), round(df.Coderre/df.total,2), 
                            np.where((df.winner == 'Bergeron'), round(df.Bergeron/df.total,2), 
                            np.where((df.winner == 'Joly'), round(df.Joly/df.total,2), 
                            'No Change')))
#print(df)

################################ Working with data election geo Json ###################################

df2 = px.data.election_geojson()
#Trying to understand how the data wokrs
#print(df2.keys())
#print(df2['features'].keys())
#print(df2['features'][0]['id'])
#print(df2['features'][0]['properties'])
#print(df2['features'][0]['geometry'])
#print(df2['features'][0]['type'])
