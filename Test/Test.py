# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import datetime
import pandas as pd
import numpy as np

N, past_num, week_num = 1133, 140, 7
X = [[i] + [1 if j == i % week_num else 0 for j in xrange(week_num)] for i in xrange(N - past_num, N)]
print X