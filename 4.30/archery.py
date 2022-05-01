def solution(n, info):
    answer = []
    temp = []

    for case in range(1024):
        binary_num = format(case, 'b')
        binary_num = binary_num.rjust(10, "0")

        temp = []
        for i in range(10):
            if binary_num[i] == "1":
                temp.append(info[i] + 1)
            else:
                temp.append(0)
        if 0 < sum(temp) <= n:
            score = 0
            enemy_score = 0
            for i in range(10):
                if temp[i] > 0:
                    score = score + (10 - i)
                elif info[i] > 0:
                    enemy_score = enemy_score + (10 - i)

            if score > enemy_score:
                temp.append(score - enemy_score)
                answer.append(temp)
    if len(answer) == 0:
        return [-1]
    else:
        return_list = []
        answer = sorted(answer, key=lambda x: -x[-1])
        max_gap = answer[0][-1]
        for i in answer:
            if i[-1] == max_gap:
                return_list.append(i[:-1])
        return_list.sort(key=lambda x: (-x[-1], -x[-2], -x[-3], -x[-4], -x[
            -5], -x[-6], -x[-7], -x[-8], -x[-9], -x[-10]))
        return_value = return_list[0]
        return_value.append(0)
        while sum(return_value) < n:
            return_value[-1] += 1
        return return_value
