import pandas_datareader as data
import pandas as pd 
import yfinance as yf
from matplotlib import pyplot as plt 
import argparse


# data_src = 'yahoo'
# start_date = '2021-01-01'
# end_date = '2025-03-17'




microsoft = yf.Ticker("MSFT")
amazon = yf.Ticker("AMZN")
nividia = yf.Ticker("NVDA")
google = yf.Ticker("GOOG")
meta = yf.Ticker("META")
apple = yf.Ticker("AAPL")

def dividends(company): 
    dividends = company.dividends
    
    if dividends.empty: 
        print(f"no data for {company.ticker}")
    else:
        dividends.plot(kind="bar", figsize=(10,5), title=f"{company}")
        plt.xlabel("Date")
        plt.ylabel("Dividend Amount")
        plt.show()


def actions_price(company):
    actions_price = company.actions
    # if company doesnt exist 
    if actions_price.empty:
        print(f"no data for {company.ticker}")
    else:
        print(actions_price)



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="")

    args = parser.parse_args()
    company = yf.Ticker(args.ticker)



    dividends(args.ticker)
    actions_price(args.ticker)





