from tkinter import *
import plotly.plotly as py
import plotly.graph_objs as go 
import pandas as pd
from datetime import datetime
import pandas.io.data as web

mGui = Tk()

mGui.geometry('651x700+51+51')
mGui.title('Plotly at Tkinter')

df = web.DataReader("AAPL", 'yahoo',
                    datetime(2007, 10, 1),
                    datetime(2016, 7, 11))

trace = go.Scatter(x=df.index,
                   y=df.High)


data = [trace]
layout = dict(
    title='Time series with range slider and selectors',
    xaxis=dict(
        rangeselector=dict(
            buttons=list([
                dict(count=1,
                     label='1m',
                     step='month',
                     stepmode='backward'),
                dict(count=6,
                     label='6m',
                     step='month',
                     stepmode='backward'),
                dict(count=1,
                    label='YTD',
                    step='year',
                    stepmode='todate'),
                dict(count=1,
                    label='1y',
                    step='year',
                    stepmode='backward'),
                dict(step='all')
            ])
        ),
        rangeslider=dict(),
        type='date'
    )
)

fig = dict(data=data, layout=layout)
py.iplot(fig)

mGui.mainloop()