#!/bin/python


A, B, C, D = sorted(map(int, raw_input().split()))
dp = [[0 for i in range(6005)] for i in range(3002)]
sm = [0 for i in range(3002)]

for i in range(C, 0, -1):
    for j in range(D, i - 1, -1):
        x = i ^ j
        dp[i][x] = dp[i + 1][x] + 1
        sm[i] += dp[i][x]
    for j in range(6005):
        if dp[i][j] == 0:
            dp[i][j] = dp[i + 1][j]
            sm[i] += dp[i][j]

total = 0
for b in range(1, B + 1):
    for a in range(1, min(b + 1, A + 1)):
        total += sm[b] - dp[b][a ^ b]
print total
