# -*- coding: utf-8 -*-
"""

"""

from dpp import *
import pandas as pd

my_kline = src_selector.choose_src('HK.00700', 'futu')
my_kline.req_hist_kline('2020-12-01', '2020-12-10')
