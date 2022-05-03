# skill의 각 행은 [type, r1, c1, r2, c2, degree]
# r1,c1 - r2,c2 까지 힐or딜
# type 1은 공격 2는 힐
# r1<=r2 & c1<=c2
# skill 은 최대 250000
# board 은 최대 1000 x 1000
# 지금 => 250000 * 1000 * 1000 번 시행중
def solution1(board, skill_list):
    answer = 0
    for skill in skill_list:
        skill_type, r1, c1, r2, c2, degree = skill
        attack = -1
        if skill[0] == 2: attack = 1
        for i in range(r1, r2 + 1):
            for j in range(c1, c2 + 1):
                board[i][j] += attack * degree
    for b in board:
        for item in b:
            if item > 0:
                answer += 1

    return answer


def solution2(board, skill_list):
    answer = 0
    n = len(board)
    m = len(board[0])
    d = [[0] * (len(board[0]) + 1) for _ in range(len(board) + 1)]
    for skill in skill_list:
        skill_type, r1, c1, r2, c2, degree = skill
        if skill[0] == 1:
            degree = -degree
        d[r1][c1] += degree
        d[r1][c2 + 1] -= degree
        d[r2 + 1][c1] -= degree
        d[r2 + 1][c2 + 1] += degree

    for i in range(len(d) - 1):
        for j in range(len(d[0]) - 1):
            d[i][j + 1] += d[i][j]

    for j in range(len(d[0]) - 1):
        for i in range(len(d) - 1):
            d[i + 1][j] += d[i][j]

    for i in range(len(board)):
        for j in range(len(board[0])):
            board[i][j] += d[i][j]
            if board[i][j] > 0:
                answer += 1
    return answer


test_board = [[5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5],
              [5, 5, 5, 5, 5]]
test_skill = [[1, 0, 0, 3, 4, 4], [1, 2, 0, 2, 3, 2], [2, 1, 0, 3, 1, 2],
              [1, 0, 1, 3, 3, 1]]

solution2(test_board, test_skill)
