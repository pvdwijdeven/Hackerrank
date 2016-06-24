# -*- coding: utf-8 -*-
"""
Image unsampling

Pascal van de Wijdeven
"""

import sys
import numpy as np
import profile


def main():
    nrows_scaled,ncols_scaled,N=map(int,f.readline().split())
    nrows_orig,ncols_orig=map(int,f.readline().split())
    scaled=np.zeros([nrows_scaled, ncols_scaled,3],dtype=int)
    orig=np.zeros([nrows_orig, ncols_orig,3],dtype=int)
    
    for r in range(nrows_scaled):
        rowOfrgbColors=((f.readline().strip()).split(" "))
        for c in range(ncols_scaled):
           scaled[r][c]=map(int,rowOfrgbColors[c].split(","))
    
    for r in range(nrows_scaled):
        for c in range(ncols_scaled):
            newColors=getColors(orig,scaled,r,c,N)
    
    for x in orig:
        for y in x:
            print( ",".join( repr(e) for e in y ) ),
        print "\n",


try:
    filename = "SampleInput.txt"
    f = open(filename)
    local=True
except:
    f= sys.stdin
    local=False
 
def getColors(orig,scaled,r,c,N):
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
    #now make borders of square
    #upper row
    for x in range(N+1):
        orig[r+0][c+x]=((N-x)*A+(x)*B)/N
        orig[r+N][c+x]=((N-x)*C+(x)*D)/N
    #now fill in inner columns
    for y in range(1,N):
        for x in range(0,N+1):
            orig[y][x]=((orig[r+0][c+x])*(N-y)+orig[r+N][c+x]*(y))/N
    return orig
if __name__ == "__main__":
    profile.run('main()')


