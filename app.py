from flask import Flask, render_template, request
import pandas as pd
import yfinance as yf
import plotly.express as px
import json

# Initialize Flask app
app = Flask(__name__)
