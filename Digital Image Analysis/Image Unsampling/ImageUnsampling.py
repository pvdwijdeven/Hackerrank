# -*- coding: utf-8 -*-
"""
Image unsampling

Pascal van de Wijdeven
"""

import sys

try:
    filename = "SampleInput.txt"
    f = open(filename)
    local=True
except:
    f= sys.stdin
    local=False
 
def getColor(r,c,N,x):
    
   
nrows_down,ncols_down,N=map(int,f.readline().split())
nrows_org,ncols_org=map(int,f.readline().split())
down=[]
for i in range(nrows_down):
    row_tuples=((f.readline().strip()).split(" "))
    row=[]
    for tups in row_tuples:
        row.append(map(int,tups.split(",")))
    down.append(row)

orig=[]
for r in range(nrows_org):
    row=[]
    for c in range(ncols_org):
        row.append([0,0,0])
    orig.append(row)


newpict=[]
for r in range(nrows_down):
    for c in range(ncols_down):
        getColor=down[r][c]
        for x in range(N):
            for y in range(N):
                if r*N+x<nrows_org and r*N+y<ncols_org: orig[r*N+x][c*N+y]=getColor#(r,c,N,x)

for x in orig:
    for y in x:
        print( ",".join( repr(e) for e in y ) ),
    print "\n",
