# bfs
from collections import deque


def dfs(board, start):
    q = deque(start)
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    place = []
    for i in board:
        place.append(list(i))
    visited = []
    while q:
        x, y = q.popleft()
        visited.append([x, y])
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < 5 and 0 <= ny < 5 and [nx, ny] not in visited:
                if place[nx][ny] == "P":
                    if place[x][y] == "P" or place[x][y] == 1:
                        return False
                if place[nx][ny] == "O":
                    try:
                        place[nx][ny] = place[x][y] + 1
                    except:
                        place[nx][ny] = 1
                    q.append([nx, ny])

    return True


def solution(places):
    answer = []
    for place in places:
        temp = []
        for i in range(len(place)):
            for j in range(len(place[i])):
                if place[i][j] == "P":
                    temp.append([i, j])
        temp_ans = []
        for x, y in temp:
            temp_ans.append(dfs(place, [[x, y]]))
        if (False in temp_ans):
            answer.append(0)
        else:
            answer.append(1)

    return answer


test_places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
               ["POOPX", "PXPXP", "PXXXO", "OXXXO", "OOOOP"],
               ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"],
               ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
               ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
test_results = [1, 0, 1, 1, 1]

print(solution(test_places))
