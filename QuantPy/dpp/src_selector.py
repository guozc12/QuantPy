# -*- coding: utf-8 -*-
"""

"""
from .src import *


def choose_src(code, src):
    if src == 'futu':
        return kline_futu.KlineFutu(code, src)
