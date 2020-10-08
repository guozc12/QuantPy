# -*- coding: utf-8 -*-
"""Playground for testing strategy

This module demonstrates: the evaluation "EVA" of a strategy "STRATE" working on an subject "SUB".


Example:
    Examples can be given using either the ``Example`` or ``Examples``
    sections. Sections support any reStructuredText formatting, including
    literal blocks::

        $ python example_google.py

Section breaks are created by resuming unindented text. Section breaks
are also implicitly created anytime a new section starts.

Attributes:
    module_level_variable1 (int): Module level variables may be documented in
        either the ``Attributes`` section of the module docstring, or in an
        inline docstring immediately following the variable.

        Either form is acceptable, but the two should not be mixed. Choose
        one convention to document module level variables and be consistent
        with it.

Todo:
    * For module TODOs
    * You have to also use ``sphinx.ext.todo`` extension

.. _Google Python Style Guide:
   http://google.github.io/styleguide/pyguide.html

"""

import pandas as pd
import numpy as np
import datetime
import pandas_datareader.data as web
import matplotlib.pyplot as plt

# Import data
# df = pd.read_csv('AAPL.csv')
start = datetime.datetime(2020, 1, 1)
stop = datetime.datetime(2020, 10, 6)
df = web.DataReader("AAPL", "yahoo", start, stop)
print(df.head())

df['Capital'] = 1

c_rate = 1.2 / 10000  # commission rate
t_rate = 1 / 1000  # stamp duty rate

df['ROI'] = df['Close']/df['Open']

