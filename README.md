## Stock-Data-Retrieval-and-Storage-in-python-from-yahoo-finance

### Video demonstration --> https://www.youtube.com/watch?v=FsNPlclRfJw

#### Task:

###### Gowtham is an algo trader who wants to perform some stock market analysis on ICICI bank. He wants to store the real-time stock market data of ICICI bank for this week in his database. For each day, he wants to store the data from 11.00 AM to 2.00 PM. However, he cannot afford to pay for a real-time API, so he decides to use the Python Yahoo Finance library which provides real-time data around a 15-minutes delay.
##### Write a Python program that will store 15-minute candle data of ICICI bank for every 15 minutes from 11.15 AM to 2.15 PM daily for a week. The program should use the Yahoo Finance library to retrieve the real-time data and store it in the database. Due to the 15-minute delay in the Yahoo Finance library, the program should start logging at 11.15 AM to capture data for the 11.00 AM time interval.

#### Note:
###### You should use MongoDB as a database and python APS Scheduler library for this task. The ticker for ICICI bank is "ICICIBANK.NS" and you can obtain stock information from Yahoo Finance using the yfinance library.
