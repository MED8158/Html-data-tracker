import numpy as np
import pandas_montecarlo 
import pandas_datareader.data as web
import datetime
import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()
stock = 'TSLA'
stock2 = 'AAPL'
start = datetime.datetime(2017, 1, 1)
end = datetime.datetime(2018, 2, 8)
df = web.DataReader(stock, 'morningstar', start, end)
df.reset_index(inplace=True)
df.set_index("Date", inplace=True)
df = df.drop("Symbol", axis=1)

df2 = web.DataReader(stock2, 'morningstar', start, end)
df2.reset_index(inplace=True)
df2.set_index("Date", inplace=True)
df2 = df2.drop("Symbol", axis=1)

app.layout = html.Div([
    html.Div([
        html.Div([
            html.H3('Tesla'),
            dcc.Graph(id='g1', figure={'data': [{'x': df.index, 'y': df.Close, 'type': 'line', 'name': stock}]},
   
        className="six columns")]),

        html.Div([
            html.H3('Apple'),
            dcc.Graph(id='g2', figure={'data': [{'x': df2.index, 'y': df2.Close, 'type': 'line', 'name': stock2}]})], 
        className="six columns")
    ], className="row")
])


if __name__ == '__main__':
    app.run_server(debug=True)
