def solution(board, moves):
    answer = 0
    result = []
    new_board = [[] for _ in range(len(board))]
    for i in range(len(board)):
        for j in range(len(board)):
            if board[j][i] != 0:
                new_board[i].append(board[j][i])
    while moves:
        move = moves.pop(0) - 1
        if len(new_board[move]) > 0:
            item = new_board[move].pop(0)
            result.append(item)
    new_result = result
    for i in range(len(result)):
        for j in range(len(result) - 1):
            try:
                if new_result[j] == new_result[j + 1]:
                    del (new_result[j:j + 2])
                    answer += 2
            except:
                pass
    return answer


board = [[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2],
         [3, 5, 1, 3, 1]]
moves = [1, 5, 3, 5, 1, 2, 1, 4]
print(solution(board, moves))