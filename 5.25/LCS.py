# https://www.acmicpc.net/problem/9251

arr1 = input()
arr2 = input()

dp = [[0] * (len(arr2) + 1) for _ in range(len(arr1) + 1)]

for i in range(1, len(arr1) + 1):
    for j in range(1, len(arr2) + 1):
        print(arr1[i - 1], arr2[j - 1])
        if arr1[i - 1] == arr2[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
    print(dp)