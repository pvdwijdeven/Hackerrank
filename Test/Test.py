# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import math

a=[1,2,3,2+2*math.sqrt(2)/3]


avg=0
for x in a:
    avg+=x
avg=avg/4.0

variance=0
for x in a:
    variance+=(avg-x)**2
variance=variance/4.0
print variance

print 2*math.sqrt(2)/3