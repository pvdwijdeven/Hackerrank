# -*- coding: utf-8 -*-
"""
Created on Fri Jul 01 18:59:15 2016

@author: PvdWijdeven
"""
debug = True
printtable=False
if debug:
    import time
    starttime=time.time()
    n = 3
    nums = [1, 2,3]
    L, R = 10,20
else:
    n = input()
    nums = map(int, raw_input().split())
    L, R = map(int, raw_input().split())

def count(S, m, n):
    # We need n+1 rows as the table is constructed in bottom up
    # manner using the base case 0 value case (n = 0)
    table = [0 for x in range(n + 1)]

    # Fill the entries for 0 value case (n = 0)
    table[0]=1

    # Fill rest of the table entries in bottom up manner
    for i in range(0,m):
        for j in range(S[i],n+1):
            table[j]+=table[j-S[i]]
    return table
""""
def count_rec(prevtable, S, m, n):
    # We need n+1 rows as the table is constructed in bottom up
    # manner using the base case 0 value case (n = 0)
    table = [0 for x in range(n + 1)]
    #table[0]=prevtable[prod]
    # Fill rest of the table entries in bottom up manner
    for i in range(0,m):
        for j in range(S[i],n+1):
            if (j-S[i])>=0:
                table[j]+=table[j-S[i]]
            else:
                table[j]+=prevtable[prod+(i-S[j])]
    return table
"""
m = len(nums)
prod = 1
for p in nums:
    prod*=p
if debug: print prod
total=0
# make first table, with range prod
table = count(nums, m, R+1)
# check if table is already sufficient or L falls within table
if debug and printtable: print table
"""
if len(table)>=R+1:
    for i in range(L,R+1):
        total+=table[i]
elif prod>=L:
    for i in range(L,prod+1):
        total+=table[i]
# recursively make other tables, with former table as input
"""
for i in range(L,R+1):
    total+=table[i]
"""
start=1
end=prod
while end<=R+1:
    start=start+prod
    end=end+prod
    table = count_rec(list(table), nums, m, prod)
    if debug and printtable: print table
    start_range=1
    end_range=prod+1
    if start+1<L: start_range=L-start+1
    if end>R+1: end_range=end_range-(end-(R))
    for i in range(start_range,end_range):
        total+=table[i]
"""
print total % (10 ** 9 + 7)
if debug: print time.time()-starttime