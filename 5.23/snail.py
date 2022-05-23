repeat = int(input())
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
for rep in range(repeat):
    n = int(input())
    arr = [[0 for __ in range(n)] for _ in range(n)]
    cnt = 1
    x, y = 0, 0
    index = 0
    for i in range(n * n):
        arr[x][y] = cnt
        cnt += 1
        nx = x + dx[index]
        ny = y + dy[index]
        if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] == 0:
            x, y = nx, ny
        else:
            index = (index + 1) % 4
            x = x + dx[index]
            y = y + dy[index]
    print(f"#{rep+1}")
    for a in arr:
        for i in a:
            print(i, end=' ')
        print()
