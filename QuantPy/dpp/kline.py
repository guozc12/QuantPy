# -*- coding: utf-8 -*-
"""

"""
import pandas as pd
import datetime


class Kline:
    def __init__(self, code, src):
        self.code = code  # code of target
        self.src = src  # data source

    # request historical kline data from src data source
    def req_hist_kline(self, start, end, ktype, autype):
        pass

    # request kline data from local data base
    def req_local_kline(self):
        pass

    # binning data from short-interval kline to long-interval kline
    def binning(self):
        pass
