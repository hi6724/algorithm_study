# https://www.acmicpc.net/problem/11053

n = int(input())
arr = list(map(int, input().split()))

ans = [0] * n

for i in range(n):
    for j in range(n):
        if arr[j] < arr[i]:
            ans[i] = max(ans[i], ans[j] + 1)
print(max(ans))
