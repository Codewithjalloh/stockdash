from flask import Flask, render_template, request
import pandas as pd
from alpha_vantage.timeseries import TimeSeries
import plotly.express as px
import json

# Initialize Flask app
app = Flask(__name__)

# Alpha Vantage API Key (replace 'YOUR_API_KEY' with your actual API key)
ALPHA_VANTAGE_API_KEY = 'YOUR_API_KEY'

# Function to fetch stock data
def fetch_stock_data(ticker):
    ts = TimeSeries(key=ALPHA_VANTAGE_API_KEY, output_format='pandas')
    data, meta_data = ts.get_daily(ticker, outputsize='compact')
    # Renaming the columns for consistency
    data.rename(columns={
        '1. open': 'Open', '2. high': 'High', 
        '3. low': 'Low', '4. close': 'Close', 
        '5. volume': 'Volume'
    }, inplace=True)
    return data

# Function to create stock graph
def create_stock_graph(df, ticker):
    fig = px.line(df, x=df.index, y='Close', title=f'Stock Price of {ticker}')
    return fig

# Route for the stock dashboard
@app.route('/', methods=['GET', 'POST'])
def stock_dashboard():
    graphJSON = ''
    if request.method == 'POST':
        ticker = request.form.get('stockTicker')
        df = fetch_stock_data(ticker)
        fig = create_stock_graph(df, ticker)
        graphJSON = json.dumps(fig, cls=px.utils.PlotlyJSONEncoder)
    return render_template('dashboard.html', graphJSON=graphJSON)

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
