import numpy as np # linear algebra
import pandas as pd # for data preparation
import plotly.express as px # for data visualization
from textblob import TextBlob # for sentiment analysis


#To read the data set
dff=pd.read_csv('netflix_titles.csv')               #We use pandas here. dff gives the dataframe
dff.columns                                            #we use dff columns here to get access the columns
print(dff.columns)

#To get distribution of content type

z = dff.groupby(['rating']).size().reset_index(name='counts')           #groupp by splitting used to slpit obj and combine res 
                                                                            #resindex used to treat index as columns

pieChart = px.pie(z, values='counts', names='rating', 
                  title='Content Ratings on Netflix',labels='Deon', 
                  color_discrete_sequence=px.colors.qualitative.Set3)
pieChart.show()

#Analyzing content

df1=dff[['type','release_year']]
df1=df1.rename(columns={"release_year": "Release Year"})

df2=df1.groupby(['Release Year','type']).size().reset_index(name='Total Content')

df2=df2[df2['Release Year']>=2010]

fig3 = px.line(df2, x="Release Year", y="Total Content", color='type',title='Trend of content produced over the years on Netflix')
fig3.show()

#Partial Presentation is Done!