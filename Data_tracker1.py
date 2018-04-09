# -*- coding: utf-8 -*-
"""
Created on Sun Apr  8 19:36:08 2018

@author: Matthew
"""

import numpy as np
import pandas_montecarlo 
import pandas_datareader.data as web
import datetime
import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()
stock = 'TSLA'
start = datetime.datetime(2017, 1, 1)
end = datetime.datetime(2018, 2, 8)
df = web.DataReader(stock, 'morningstar', start, end)
df.reset_index(inplace=True)
df.set_index("Date", inplace=True)
df = df.drop("Symbol", axis=1)



app.layout = html.Div([
    html.Div([
        html.Div(
            html.H3('Column 1'),
            dcc.Graph(id='g1', figure={'data': [{'x': df.index, 'y': df.Close, 'type': 'line', 'name': stock}]}
   
        ], className="six columns"),

        html.Div([
            html.H3('Column 2'),
            dcc.Graph(id='g2', figure={'data': [{'y': [1, 2, 3]}]})
        ], className="six columns"),
    ], className="row")
])


if __name__ == '__main__':
    app.run_server(debug=True)
    
 
