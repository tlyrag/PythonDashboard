from encodings import CodecRegistryError
import plotly.express as px
import pandas as pd
import numpy as np


df = px.data.election()
df_top5 = df.head()

#print(df.head())


## Possible Columns winner_percentage, winner_votes, candidate_percentage, 
## Adding Columns to dataframe
df['Coderre_percentage'] = round(df.Coderre/df.total,2)
df['Bergeron_percentage'] = round(df.Bergeron/df.total,2)
df['Joly_percentage'] = round(df.Joly/df.total,2)
#print(df)


df['winner_votes'] = np.where((df.winner =='Coderre'), df.Coderre, 
                     np.where((df.winner == 'Bergeron'), df.Bergeron, 
                     np.where((df.winner == 'Joly'), df.Joly, 
                     'No Change')))

df['winner_percentage'] =   np.where((df.winner =='Coderre'), round(df.Coderre/df.total,2), 
                            np.where((df.winner == 'Bergeron'), round(df.Bergeron/df.total,2), 
                            np.where((df.winner == 'Joly'), round(df.Joly/df.total,2), 
                            'No Change')))
print(df)