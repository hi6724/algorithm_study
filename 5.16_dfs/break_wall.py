# https://www.acmicpc.net/problem/2206

import copy
from collections import deque

n, m = map(int, input().split())
wall_list = []
arr = []
for i in range(n):
    arr.append(list(map(int, list(input()))))
for i in range(n):
    for j in range(m):
        if (arr[i][j] == 1):
            wall_list.append([i, j])
# 모든 벽을 하나씩 부숴가면서 반복함
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
ans = -1

for wall in wall_list:
    wx, wy = wall
    temp = copy.deepcopy(arr)
    temp[0][0] = 1
    temp[wx][wy] = 0
    q = deque()
    q.append([0, 0])
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if temp[nx][ny] == 0:
                    temp[nx][ny] = temp[x][y] + 1
                    q.append([nx, ny])

    if temp[n - 1][m - 1] != 0 and temp[n - 1][m - 1] > ans:
        ans = temp[n - 1][m - 1]
print(ans)
