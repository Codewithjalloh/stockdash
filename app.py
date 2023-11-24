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
