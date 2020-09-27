"""
This function is for getting realtime stock data
data source is sinajs
"""

import pandas as pd
from urllib.request import urlopen

# data from sina
# http://hq.sinajs.cn/list=sh600000,hk01810,gb_tsla
# https://finance.sina.com.cn/realstock/company/hk01810/nc.shtml

# get data
url = "http://hq.sinajs.cn/list=sh600000,sz000002,gb_tsla,hk01810,hk00700,gb_ba,gb_nio,gb_twtr,hk00066,hk03690"
content = urlopen(url).read().decode('gbk')


# clean data
data_line = content.strip().split('\n')
data_line = [i.replace('var hq_str_', '').split(',') for i in data_line]
df = pd.DataFrame(data_line, dtype='float')

df[0] = df[0].str.split('="')
df['stock_code'] = df[0].str[0].str.strip()
df['stock_name'] = df[0].str[-1].str.strip()
df['candle_end_time'] = pd.to_datetime(df[30] + ' ' + df[31])

rename_dict = {1: 'open', 2: 'pre_close', 3: 'close', 4: 'high', 5: 'low', 6: 'buy1', 7: 'sell1',
                8: 'amount', 9: 'volume', 32: 'status'}
df.rename(columns=rename_dict, inplace=True)
df['status'] = df['status'].str.strip('";')
df = df[['stock_code', 'stock_name', 'candle_end_time', 'open', 'high', 'low', 'close', 'pre_close', 'amount', 'volume',
          'buy1', 'sell1', 'status']]

# print data
with pd.option_context('display.max_rows', None, 'display.max_columns', None):
    print(df)

# save data
df.to_csv('stock_data.csv', index=False)



