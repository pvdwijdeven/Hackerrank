# -*- coding: utf-8 -*-
"""
Created on Fri Jun 24 15:16:07 2016

@author: pvandewijdeven
"""


import sys
import os
import numpy
import profile
from scipy.interpolate import RectBivariateSpline

try:
    filename = "SampleInput2.txt"
    f = open(filename)
    local=True
except:
    f= sys.stdin
    local=False

def main():
    rows, cols, n = map(int, f.readline().split())
    rows_t, cols_t = map(int, f.readline().split())
    
    re_pixels = numpy.zeros(shape=(rows,cols))
    gr_pixels = numpy.zeros(shape=(rows,cols))
    bl_pixels = numpy.zeros(shape=(rows,cols)) 
    r = 0;
    for r in range(0,rows):
        line = f.readline()
        pixels = line.split()
        for c in range(0,cols) :
            re, gr, bl = map(int, pixels[c].split(","))
            re_pixels[r,c] = re
            gr_pixels[r,c] = gr
            bl_pixels[r,c] = bl
    
    row_indicies = numpy.arange(0, rows_t, n)
    row_indicies = row_indicies[:rows]
    col_indicies = numpy.arange(0, cols_t, n)
    col_indicies = col_indicies[:cols]
    
    interpolation = 1
    
    f_re = RectBivariateSpline(row_indicies, col_indicies, re_pixels, kx=interpolation, ky=interpolation)
    re_predict = f_re(numpy.arange(0, rows_t), numpy.arange(0, cols_t))
    f_gr = RectBivariateSpline(row_indicies, col_indicies, gr_pixels, kx=interpolation, ky=interpolation)
    gr_predict = f_gr(numpy.arange(0, rows_t), numpy.arange(0, cols_t))
    f_bl = RectBivariateSpline(row_indicies, col_indicies, bl_pixels, kx=interpolation, ky=interpolation)
    bl_predict = f_bl(numpy.arange(0, rows_t), numpy.arange(0, cols_t))
    
    results = []
    for r in range(0,rows_t):
        for c in range(0,cols_t):
            results.append(str(int(round(re_predict[r,c]))) + "," + str(int(round(gr_predict[r,c]))) + "," + str(int(round(bl_predict[r,c]))) + " ")
        results.append("\n")
        
    os.write(1, str.join('', results))
    
if __name__ == "__main__":
    profile.run('main()')