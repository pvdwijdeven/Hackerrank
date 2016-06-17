# -*- coding: utf-8 -*-
"""
Created on Thu Jun 16 23:43:29 2016

@author: Gebruiker
"""
import nltk 
import sys
import re

n3grams=[' th','he ',' s ','ed ',' of',' an','of ','nd ',' in',' to','ing','ng ','er ','to ','on ','in ','is ',' a ',' co','es ','ion','re ','as ','at ','ent',' be','tio','or ',' he',' re','ly ',' ha',' fo']

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
#print z.replace("\n"," ")
z = z.decode('utf-8')
z= nltk.tokenize.word_tokenize(z)
fdist1 = nltk.FreqDist(z)

x= fdist1.most_common(10000)

value=[]
for y in x:
    curval=((len(y[0])*9)-17)*y[1]
    value.append((y[0],curval))

x=  sorted(value, key=lambda val: val[1],reverse=True) 
#print x
s=0
for y in x[0:3000]:
    if len(y[0])>=3:
        print '"' + y[0] + '":'+ str(s) + ",",
        s=s+1
print
        
for y in n3grams:
    print '"' + y + '":' + str(s) + ",",
    s=s+1
    
for y in x[0:3000]:
    for z in n3grams:
        if y[0]==z:
            print z