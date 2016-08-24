"""
Normalize data
24-08-2016
PvdWijdeven
"""

import numpy as np
from sklearn.preprocessing import normalize

def filter_data(filename, columns):
    # filters data with only required columns
    # todo: create numpy array
    indices = []
    try:
        with open(filename, 'r') as f:
            all_headers = f.readline().split(",")
            # first item is Id, last one is Response
            headers = []
            for idx, label in enumerate(all_headers):
                if label in columns:
                    indices.append(idx)
                    headers.append(label)
            idx_response=len(all_headers)-1
            data = [headers]
            Ids=[]
            Responses=[]
            for line in f:
                cur_data = []
                cur_line = line.split(",")
                for idx, element in enumerate(cur_line):
                    if idx==0:
                        Ids.append(element)
                    elif idx==idx_response:
                        Responses.append(element)
                    if idx in indices:
                        cur_data.append(element)
                data.append(cur_data)
    except IOError:
        exit("Aborting... file %s not found" % filename)
    return np.array(data)


my_data = filter_data("H:\\R\\Kaggle\\Bosch\\data\\training\\test.csv", ["L3_S32_D3852", "L3_S32_F3850"])
my_data=normalize(my_data, norm='l2')

