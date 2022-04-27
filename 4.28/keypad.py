def calc_distance(list_a, list_b):
    distance = 0
    for i in range(2):
        distance += abs(list_b[i] - list_a[i])
    return distance


def solution(numbers, hand):
    answer = ""
    pos_obj = {
        1: (-1, 3),
        2: (0, 3),
        3: (1, 3),
        4: (-1, 2),
        5: (0, 2),
        6: (1, 2),
        7: (-1, 1),
        8: (0, 1),
        9: (1, 1),
        0: (0, 0),
    }
    left_pos = (-1, 0)
    right_pos = (1, 0)
    while numbers:
        number = numbers.pop(0)
        if pos_obj[number][0] < 0:
            answer += "L"
            left_pos = pos_obj[number]
        if pos_obj[number][0] > 0:
            answer += "R"
            right_pos = pos_obj[number]
        if pos_obj[number][0] == 0:
            left_distacne = calc_distance(pos_obj[number], left_pos)
            right_distacne = calc_distance(pos_obj[number], right_pos)
            if left_distacne < right_distacne:
                answer += "L"
                left_pos = pos_obj[number]
            if right_distacne < left_distacne:
                answer += "R"
                right_pos = pos_obj[number]
            if left_distacne == right_distacne:
                if hand == "right":
                    answer += "R"
                    right_pos = pos_obj[number]

                else:
                    answer += "L"
                    left_pos = pos_obj[number]

    return answer


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
hand = 'right'
print(solution(numbers, hand))
