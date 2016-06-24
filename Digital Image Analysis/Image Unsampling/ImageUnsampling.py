# -*- coding: utf-8 -*-
"""
Image unsampling

Pascal van de Wijdeven
"""

import sys
import numpy as np

try:
    filename = "SampleInput.txt"
    f = open(filename)
    local=True
except:
    f= sys.stdin
    local=False
 
def getColors(scaled,r,c,N):
    result=[]
    A=scaled[r][c]
    #first get neighbours
    if c+1<len(scaled[0]):
        B=scaled[r][c+1]
    else:
        B=A
    if r+1<len(scaled):
        C=scaled[r+1][c]
    else:
        C=A
    if c+1<len(scaled[0])and r+1<len(scaled):
        D=scaled[r+1][c+1]
    else:
        D=A
    A=np.array(A)
    B=np.array(B)
    C=np.array(C)
    D=np.array(D)
    row_result=[]
    #now make borders of square
    #upper row
    for x in range(N+1):
        row_result.append(((N-x)*A+(x)*B)/N)
    result.append(row_result)
    #create dummy inner rows
    for y in range(1,N):
        row_result=[]
        for x in range(N+1):
            row_result.append(A)
        result.append(row_result)
    #lower row
    row_result=[]
    for x in range(N+1):
        row_result.append(((N-x)*C+(x)*D)/N)
    result.append(row_result)

    #now fill in inner columns
    for y in range(1,N):
        for x in range(0,N+1):
            tempA=np.array(result[0][x])
            tempB=np.array(result[N][x])
            result[y][x]=(tempA*(N-y)+tempB*(y))/N
    return result



nrows_scaled,ncols_scaled,N=map(int,f.readline().split())
nrows_org,ncols_org=map(int,f.readline().split())
scaled=[]
for i in range(nrows_scaled):
    row_tuples=((f.readline().strip()).split(" "))
    row=[]
    for tups in row_tuples:
        row.append(map(int,tups.split(",")))
    scaled.append(row)


orig=[]
for r in range(nrows_org):
    row=[]
    for c in range(ncols_org):
        row.append([0,0,0])
    orig.append(row)


newpict=[]
for r in range(nrows_scaled):
    for c in range(ncols_scaled):
        newColors=getColors(scaled,r,c,N)
        for x in range(N):
            for y in range(N):
                if r*N+x<nrows_org and c*N+y<ncols_org: 
                    orig[r*N+x][c*N+y]=newColors[x][y]

for x in orig:
    for y in x:
        print( ",".join( repr(e) for e in y ) ),
    print "\n",
