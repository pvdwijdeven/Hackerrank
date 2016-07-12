#!/bin/python

import sys

n1,n2,n3 = raw_input().strip().split(' ')
n1,n2,n3 = [int(n1),int(n2),int(n3)]
h1 = map(int,raw_input().strip().split(' '))
h2 = map(int,raw_input().strip().split(' '))
h3 = map(int,raw_input().strip().split(' '))
done = False
s1=sum(h1)
s2=sum(h2)
s3=sum(h3)

while not done:
    if s1==s2 and s1==s3: 
        done=True
    else:
        if s1>s2 and s1>s3:
            s1-=h1.pop(0)
        if s2>s1 and s2>s3:
            s2-=h2.pop(0)
        if s3>s2 and s3>s1:
            s3-=h3.pop(0)
print s1