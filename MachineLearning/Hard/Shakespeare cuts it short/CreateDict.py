# -*- coding: utf-8 -*-
"""
Created on Thu Jun 16 23:43:29 2016

@author: Gebruiker
"""
from nltk import *
import sys
import re

shake_dict={"Shakespeare": 1}

def checkword(line):
        if re.match(r'^Shakespeare', line):
            return "Shakespeare"
        else:
            return ""

filename = "Sample1.txt"
f = open(filename)
    
x=f.readlines()
z="" 
for y in x:
    z=z+y
print z.replace("\n"," ")
z= nltk.tokenize.word_tokenize(z)
fdist1 = FreqDist(z)
print fdist1
x= fdist1.most_common(1000)
s=0
for y in x:
    if len(y[0])>=2:
        print '"' + y[0] + '":'+ str(s) + ",",
        s=s+1
        