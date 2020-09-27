"""This function is for getting historical data of stocks"""

import tushare as ts

mytoken = 'ecd07cde131c84a0419eae37bcd2f231ca2553c5e47b0061c511280a'
pro = ts.pro_api(mytoken)
data = pro.us_daily(ts_code='AAPL', start_date='20190101', end_date='20200928')

print(data)

#data.to_csv('600848.csv',index=False)