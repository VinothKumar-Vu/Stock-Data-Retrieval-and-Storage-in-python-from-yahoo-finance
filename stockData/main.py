'''
There are several columns that are commonly used when performing stock market analysis. Some examples include:

Date,time,current price,open_price,previous closed price,Highest of the day ,lowest of the day, and current volume of shares trading
'''

import warnings
import dateparser

# Ignore dateparser warnings regarding pytz
warnings.filterwarnings(
    "ignore",
    message="The localize method is no longer necessary, as this time zone supports the fold attribute",
)

import yfinance as yf
import datetime
from datetime import date
from apscheduler.schedulers.blocking import BlockingScheduler
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client.iciciDB
collection = db.candleData

# Define the function to retrieve and store the stock data
def task():
    # Get the current time
    now = datetime.datetime.now()

    # Get the candle data for ICICI bank from Yahoo Finance
    ticker = "ICICIGI.NS"
    stock = yf.Ticker(ticker)
    live_price = stock.info['regularMarketPrice']
    Open_price = stock.info['regularMarketOpen']
    Highest_price=stock.info['regularMarketDayHigh']
    Close_price=stock.info['regularMarketPreviousClose']
    Volume=stock.info['regularMarketVolume']
    Lowest_price = stock.info['regularMarketDayLow']
    time = now.strftime("%H:%M:%S")
    date = now.strftime("%Y-%m-%d")
    candlestick = {"Date": date, "Time": time, "Current_price": live_price, "Open": Open_price, "Close": Close_price, "Highest": Highest_price, "Lowest": Lowest_price, "Volume": Volume}

    # Insert dictionary into MongoDB
    collection.insert_one(candlestick)

    #printing values inserted into MangoDB
    print(candlestick)

scheduler = BlockingScheduler()
start_date = date.today()

# Schedule the function to run every 15 minutes for 5 day from 11:15 AM to 2:15 PM
for day in (1,6):
    scheduler.add_job(task, 'interval', minutes=15, start_date =f"{start_date} 11:15:00", end_date=f"{start_date} 14:15:00")
    scheduler.start()




