# -*- coding: utf-8 -*-
"""
Created on Thu Jun 16 21:23:50 2016

@author: Pascal van de Wijdeven
"""

import sys
import re

shake_dict={"Shakespeare": "10000000000000001"}

def checkword(line):
        if re.match(r'^Shakespeare', line):
            return "Shakespeare"
        else:
            return ""

try:
    filename = "SampleInput.txt"
    f = open(filename)
except:
    f= sys.stdin

original_text=f.readlines()
output_text=""
for x in original_text:
    i=0
    while i<len(x):
        found=checkword(x[i:])
        i=i+len(found)
        if found=="":
            output_text+= "{0:09b}".format(ord(x[i]))
            #output_text+=x[i]
            i=i+1
        else:
            #output_text+="1"+bin(1)
            output_text+=shake_dict[found]
    output_text+="{0:09b}".format(ord("\n"))
print 1
print "Shakespeare 10000000000000001"
print output_text
