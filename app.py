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
