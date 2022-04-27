import itertools


def solution(orders, course):
    answer = []
    com_num = {}
    temp = {}
    for num in course:
        com_num[num] = 0
        temp[num] = []
    for num in course:
        answer_dict = {}
        for order in orders:
            order = sorted(order)
            combination_list = list(itertools.combinations((order), num))
            for combination_item in combination_list:
                try:
                    answer_dict[
                        combination_item] = answer_dict[combination_item] + 1
                except:
                    answer_dict[combination_item] = 1
            # print(combination_list)
        for i in answer_dict:
            if com_num[num] <= answer_dict[i]:
                com_num[num] = answer_dict[i]
                temp[num].append((i, answer_dict[i]))

    for i in temp:
        for j in temp[i]:
            if (j[1] >= com_num[i] and j[1] > 1):
                temp_text = ''
                for k in j[0]:
                    temp_text += k
                answer.append(temp_text)
    answer = sorted(answer)
    return answer


# result = list(itertools.combinations(('abcde'), 2))
# print("**경우의 수 : %s개" % len(result))
# print(result)

orders = ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"]
course = [2, 3, 5]
print(solution(orders, course))
