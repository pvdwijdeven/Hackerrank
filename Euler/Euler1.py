# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

N = int(raw_input())
for i in xrange(N):
    N = long(raw_input())-1
    N3=long((N/3))
    N5=long((N/5))
    N15=long((N/15))
    total3=((1+N3)*3*N3)//2
    total5=((1+N5)*5*N5)//2
    total15=((1+N15)*15)*N15//2
    print long(total3+total5-total15)
 