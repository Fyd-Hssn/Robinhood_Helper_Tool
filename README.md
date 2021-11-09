# Robinhood_Helper_Tool
[Github Repository](https://github.com/Fyd-Hssn/Robinhood_Helper_Tool)
## Table of Contents
1. Introduction
2. Setup
## 1. Introduction
Robinhood Helper Tool was initially created to track accumulated returns from options over the lifetime of a Robinhood Brokerage Account. 
There are additional quality of life features outlined below that are built into the tool to help users concisely see certain data.

### List of Features
- ***Options Return Tracker***
  + Exports CSV for the current date that retroactively records all options trades since the creation of the Robinhood account. Here you can display either the total returns or
  returns made through a specific options strategy.
- ***Options Return by Ticker***
  + Similar to the Options Return Tracker but categorizes returns by a specific ticker instead of the overall account.
- ***Underlying Asset Return***
  + Displays current equity value and provides the $ amount needed to break-even for the total holdings. Additionally, you can display the equity return associated with a ticker
  and the options return generated from the same ticker to get a combined return value.
- ***Call/Put Premium Ratios***
  + These pages (separated into two) will display the stocks in a selected watchlist from your account, along with their current Share Price, the nearest OTM Strike Price, and the ratio %
  of the OTM Strike Price to the current Share Price. You have to enter a valid expiration date first.
- ***Portfolio/Watchlist Earnings Dates***
  + These two pages conveniently and chronologically display the upcoming earnings dates for companies in the selected list.  
  
  
The underlying functionality of this tool was developed around the [Robin Stocks API](https://robin-stocks.readthedocs.io/en/latest/index.html).

## 2. Setup
FOR FIRST TIME USERS - you will need to enter your username and password into the ***config.py*** file, and replace the placeholder values (do **NOT** change the key, only the value) in quotation marks like so:  
- config = {"USERNAME": "Enter your username here", "PASSWORD": "Enter your password here"}  

Once your credentials are entered, open up ***RH_Tool.py*** in your editor and run it. Your computer will create a pickle file as an authentication token and subsequent logins will load up the pickle file.

**NOTE**: If your Robinhood account has MFA enabled, you will be prompted to enter the MFA code in the terminal of your editor, which will be sent to you through SMS or e-mail.

You are now able to navigate the app and use its features! Make sure that you always **Export** your options data under the "Options Return Tracker" tab so that your data can be extracted. This must be done each new day you start up the app, since the exported CSV file is tied to the current date.

Note that some features such as the Call/Put Ratios tabs and the Earnings Date Tabs will require you to have watchlists in your Robinhood or current holdings.
