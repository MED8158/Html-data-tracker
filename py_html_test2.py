# -*- coding: utf-8 -*-
"""
Created on Sun Apr  8 22:48:57 2018

@author: Matthew
"""

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

app.layout = html.Div(children=[
    html.H1(children='Tesla Stock Price'),

    html.Div(children='''
        From January 1st, 2017 to Feburary 8th, 2018.
    '''),

    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': df.index, 'y': df.Close, 'type': 'line', 'name': stock},
            ],
            'layout': {
                'title': stock
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)