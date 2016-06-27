# -*- coding: utf-8 -*-
"""
Image unsampling

Pascal van de Wijdeven
"""

import sys
import numpy as np
import profile
import os


def main():
    nrows_scaled,ncols_scaled,N=map(int,f.readline().split())
    nrows_orig,ncols_orig=map(int,f.readline().split())
    scaled=np.zeros([nrows_scaled, ncols_scaled,3],dtype=int)
    
    for r in range(nrows_scaled):
        rowOfrgbColors=((f.readline().strip()).split(" "))
        for c in range(ncols_scaled):
           scaled[r][c]=map(int,rowOfrgbColors[c].split(","))
    
    results=[]
    for r in range(nrows_orig):
        results.append("")
    for r in range(nrows_scaled):
        for c in range(ncols_scaled):
            results=getColors(results,scaled,r,c,N,nrows_orig,ncols_orig,nrows_scaled,ncols_scaled)
        results[r]+="\n"
    os.write(1, str.join('', results))


try:
    filename = "SampleInput.txt"
    f = open(filename)
    local=True
except:
    f= sys.stdin
    local=False
 
def getColors(results,scaled,r,c,N,nrows_orig,ncols_orig,nrows_scaled,ncols_scaled):
    A=np.array(scaled[r][c])
    #first get neighbours
    if c+1<ncols_scaled:
        B=np.array(scaled[r][c+1])
    else:
        B=A
    if r+1<nrows_scaled:
        C=np.array(scaled[r+1][c])
    else:
        C=A
    if c+1<ncols_scaled and r+1<nrows_scaled:
        D=np.array(scaled[r+1][c+1])
    else:
        D=A
    #now make borders of square
    #upper row
    for x in range(N+1):
        results[r]=results[r]+" "+str(((N-x)*A+(x)*B)/N)
        results[r+N]=results[r+N]+" "+str(((N-x)*C+(x)*D)/N)        
    #now fill in inner columns
#    for y in range(1,N):
#        for x in range(0,N+1):
#            orig[y][x]=((orig[r][c+x])*(N-y)+orig[r+N][c+x]*(y))/N
    return results
if __name__ == "__main__":
    profile.run('main()')


