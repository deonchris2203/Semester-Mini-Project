import numpy as np                      # linear algebra
import pandas as pd                      # for data preparation
import plotly.express as px                      # for data visualization
from textblob import TextBlob                       # for sentiment analysis
from tkinter import *                       #GUI
from tkinter import messagebox                      #GUI

#To read the data set
dff=pd.read_csv('netflix_titles.csv')               #We use pandas here. dff gives the dataframe
dff.columns                                            #we use dff columns here to get access the columns

#GUI 
top = Tk()  
  
#THE MAIN WINDOW

top.title("Deon Chris")
window_width = 500
window_height = 300




# get the screen dimension
screen_width = top.winfo_screenwidth()
screen_height = top.winfo_screenheight()

# find the center point
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)

# set the position of the window to the center of the screen
top.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

# NO RESIZE
top.resizable(False, False)

#ICON
top.iconbitmap("./assets/dc.ico")




#BUTTONS 
def Content_Rating():  
    messagebox.showinfo("Deon", "Content Ratings clicked \nPlease Wait for the Rating to appear...")  
    
    #To get distribution of content type
    z = dff.groupby(['rating']).size().reset_index(name='counts')           #groupp by splitting used to slpit obj and combine res 
                                                                            #resindex used to treat index as columns

    pieChart = px.pie(z, values='counts', names='rating', 
                      title='Content Ratings on Netflix',labels='Deon', 
                      color_discrete_sequence=px.colors.qualitative.Set3)
    pieChart.show()

def Trend():  
    messagebox.showinfo("Deon", "Trend button clicked \nPlease wait for the result to be displayed.")  
    
    #Analyzing content Trend
    df1=dff[['type','release_year']]
    df1=df1.rename(columns={"release_year": "Release Year"})

    df2=df1.groupby(['Release Year','type']).size().reset_index(name='Total Content')

    df2=df2[df2['Release Year']>=2010]

    fig3 = px.line(df2, x="Release Year", y="Total Content", color='type',title='Trend of content produced over the years on Netflix')
    fig3.show()

def Top_Directors():  
    messagebox.showinfo("Deon", "Top 5 Directors clicked \nPlease wait for the result to be displayed.")  
    #Top 5 Directors
    dff['director']=dff['director'].fillna('No Director Specified')
    filtered_directors=pd.DataFrame()
    filtered_directors=dff['director'].str.split(',',expand=True).stack()
    filtered_directors=filtered_directors.to_frame()
    filtered_directors.columns=['Director']
    directors=filtered_directors.groupby(['Director']).size().reset_index(name='Total Content')
    directors=directors[directors.Director !='No Director Specified']
    directors=directors.sort_values(by=['Total Content'],ascending=False)
    directorsTop5=directors.head()
    directorsTop5=directorsTop5.sort_values(by=['Total Content'])
    fig1=px.bar(directorsTop5,x='Total Content',y='Director',title='Top 5 Directors on Netflix')
    fig1.show()

def Top_Actors():  
    messagebox.showinfo("Deon", "Top 5 Actors clicked \nPlease wait for the result to be displayed.")  
    #Top 5 Succesful actors
    dff['cast']=dff['cast'].fillna('No Cast Specified')
    filtered_cast=pd.DataFrame()
    filtered_cast=dff['cast'].str.split(',',expand=True).stack()
    filtered_cast=filtered_cast.to_frame()
    filtered_cast.columns=['Actor']
    actors=filtered_cast.groupby(['Actor']).size().reset_index(name='Total Content')
    actors=actors[actors.Actor !='No Cast Specified']
    actors=actors.sort_values(by=['Total Content'],ascending=False)
    actorsTop5=actors.head()
    actorsTop5=actorsTop5.sort_values(by=['Total Content'])
    fig2=px.bar(actorsTop5,x='Total Content',y='Actor', title='Top 5 Actors on Netflix')
    fig2.show()

def Sentiment():  
    messagebox.showinfo("Deon", "Sentiment Analysis Clicked \nPlease wait for the result to be displayed.")    
    #Sentiment Analysis
    dfx=dff[['release_year','description']]
    dfx= dfx.rename(columns={'release_year':'Release Year'})
    for index,row in dfx.iterrows():
        z=row['description']
        testimonial=TextBlob(z)
        p=testimonial.sentiment.polarity
        if p==0:
            sent='Neutral'
        elif p>0:
            sent='Positive'
        else:
            sent='Negative'
        dfx.loc[[index,2],'Sentiment']=sent


    dfx=dfx.groupby(['Release Year','Sentiment']).size().reset_index(name='Total Content')

    dfx=dfx[dfx['Release Year']>=2010]
    fig4 = px.bar(dfx, x="Release Year", y="Total Content", color="Sentiment", title="Sentiment of content on Netflix")
    fig4.show()


#BUTTON PROP  
b1 = Button(top,text = "Content Ratings",command = Content_Rating,activeforeground = "red",activebackground = "pink",pady=10, height=1, width=15)  
  
b2 = Button(top, text = "Trend",command=Trend, activeforeground = "blue",activebackground = "pink",pady=10, height=1, width=15)  
  
b3 = Button(top, text = "Top Directors", command=Top_Directors, activeforeground = "green",activebackground = "pink",pady = 10, height=1, width=15)  
  
b4 = Button(top, text = "Top 5 Actors", command=Top_Actors, activeforeground = "yellow",activebackground = "pink",pady = 10, height=1, width=15)  

b5 = Button(top, text = "Sentiment Analysis", command=Sentiment, activeforeground = "yellow",activebackground = "pink",pady = 10, height=1, width=15)

#BUTTON PACKING 
b1.pack()   
b2.pack()  
b3.pack()  
b4.pack()  
b5.pack()
  
top.mainloop()  