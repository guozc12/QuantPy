"""This function is for plotting candle chart which imported from a CSV file"""

import pandas as pd
import mplfinance as mpf

# read in data by pandas
stock_data = pd.read_csv('sh600000.csv',
                         parse_dates=['交易日期'])
print(stock_data)

# plot candle chart
my_color = mpf.make_marketcolors(up='red', down='green')
my_style = mpf.make_mpf_style(marketcolors=my_color)
title = 'SH600000'
stock_data.set_index('交易日期', inplace=True)
mpf.plot(stock_data, type='candle', title=title, ylabel="price", style=my_style)
