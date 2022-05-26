# https://www.acmicpc.net/problem/12865

import itertools

n, k = map(int, input().split())
dp = [[0] * (k + 1) for _ in range(n + 1)]
arr = []
for i in range(1, n + 1):
    w, v = map(int, input().split())
    for j in range(1, k + 1):
        if j < w:
            dp[i][j] = dp[i - 1][j]
        else:
            # ex 지금 값이 w=3 v=7 일때 j 가 4=> dp[i-1][1]+7 이랑 dp[i-1][j] 중에 큰값
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w] + v)
print(dp[n][k])