# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 22:28:07 2016

@author: Pascal van de Wijdeven
"""

import sys

filename = "SampleInput.txt"
f= sys.stdin
#f = open(filename)
Descriptions=f.readline().split(".")
for x in Descriptions:
    x.replace("\n","").lower()
Questions=[]
for _ in range(5):
    Questions.append(f.readline())
Answers=f.readline().split(";")

