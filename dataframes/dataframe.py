from encodings import CodecRegistryError
import plotly.express as px
import pandas as pd
import numpy as np
import json

################################ Working with data election ###################################
df = px.data.election()
df_top5 = df.head()
df = df.sort_values(by=['district_id'])
##df['state_id']= df['district'].str.split('-', expand = True)[0]
##print(df)
## Possible Columns winner_percentage, winner_votes, candidate_percentage, 
## Adding Columns to dataframe
df['Coderre_percentage'] = round(df.Coderre/df.total,2)
df['Bergeron_percentage'] = round(df.Bergeron/df.total,2)
df['Joly_percentage'] = round(df.Joly/df.total,2)

df['winner_votes'] = np.where((df.winner =='Coderre'), df.Coderre, 
                     np.where((df.winner == 'Bergeron'), df.Bergeron, 
                     np.where((df.winner == 'Joly'), df.Joly, 
                     'No Change')))

df['winner_percentage'] =   np.where((df.winner =='Coderre'), round(100*df.Coderre/df.total), 
                            np.where((df.winner == 'Bergeron'), round(100*df.Bergeron/df.total), 
                            np.where((df.winner == 'Joly'), round(100*df.Joly/df.total), 
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
#print(df.keys())
#print(df[0])
#print(df2['features'][0])

############################## Creating sub datasets ########################################

#print(df.winner.unique())
df_total_votes = pd.DataFrame({
    'name':['Joly', 'Coderre' ,'Bergeron'],
    'total_votes':[df.Joly.sum(),df.Coderre.sum(),df.Bergeron.sum()],
    'total_percentage':[
         round(df.Joly.sum()*100/df.total.sum())
        ,round(df.Coderre.sum()*100/df.total.sum())
        ,round(df.Bergeron.sum()*100/df.total.sum())
    ],
    'total_winner_district':df.winner.value_counts()
})
#print(df[df['district'] == '94-Jeanne-Sauvé'].winner_votes)
#print(df_total_votes)
#print(df['winner_percentage'])
df_district_votes = []
def df_district_constructor(district):
    
    df_district = df[df['district']== district]
    
    df_district_votes = pd.DataFrame({
        'name':['Joly', 'Coderre' ,'Bergeron'],
        'total_votes':[df_district.Joly.sum(),df_district.Coderre.sum(),df_district.Bergeron.sum()],
        'total_percentage':[df_district.Joly_percentage.sum(),df_district.Coderre_percentage.sum(),df_district.Bergeron_percentage.sum()]
    })

    return df_district_votes




