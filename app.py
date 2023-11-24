from flask import Flask, render_template, request
import pandas as pd
import yfinance as yf
import plotly.express as px
import json

# Initialize Flask app
app = Flask(__name__)

# Function to fetch stock data
def fetch_stock_data(ticker):
    stock = yf.Ticker(ticker)
    hist = stock.history(period="1mo")
    return hist

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
