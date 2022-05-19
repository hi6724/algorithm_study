# https://www.acmicpc.net/problem/2644

import sys
from collections import deque

sys.setrecursionlimit(300000)

n = int(input())
graph = [[] for _ in range(n + 1)]
s, e = map(int, input().split())
for _ in range(int(input())):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
ans = [0] * (n + 1)
q = deque()
q.append(n)

while q:
    node = q.popleft()
    arr = graph[node]
    for i in arr:
        if ans[i] == 0:
            ans[i] = ans[node] + 1
            q.append(i)

print(ans)