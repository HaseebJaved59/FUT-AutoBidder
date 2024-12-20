# FUT-AutoBidder

**FUT-AutoBidder** is a Python script that automates the bidding process in the EA FIFA Ultimate Team (FUT) Web App. It continuously checks the transfer market, attempts to place bids, and handles price updates based on configurable conditions.

## Features
- **Automatic Bidding**: Automatically scans the transfer market and places bids based on the minimum price, buy-now price, and bid increments.
- **Login Detection**: The script waits for the user to log in and recognizes their club name.
- **Price Validation**: It checks price conditions such as increments (100 coins, 250 coins, or 500 coins depending on the range).
- **Error Handling**: Handles various errors such as expired items or "No results found" messages.

## Prerequisites
- Python 3.x
- Selenium
- undetected-chromedriver
- Google Chrome installed
