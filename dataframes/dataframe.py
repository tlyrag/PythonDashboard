import plotly.express as px
import pandas as pd


df_teste = px.data.iris()

df_teste_list = df_teste.columns.values.tolist()
print(df_teste['species'])


