import pandas as pd
import plotly.express as px                      # for data visualization
from textblob import TextBlob  
from IPython.display import display


df=pd.read_csv('netflix_titles.csv')               #We use pandas here. dff gives the dataframe
print(df.columns)

df2 = pd.DataFrame().assign(release=df['release_year'], description=df['description'])
print(df2)

grouped = df.groupby('type').size().reset_index(name='Total Content')
grouped = grouped.loc[grouped['type'] == "Movie"]
print(grouped)

frames=(grouped, df2)
dff= pd.DataFrame(frames)
display(dff)