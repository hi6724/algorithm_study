import copy


def get_com(can_go, info, ans_lists):
    return_list = []
    while ans_lists:
        input()
        ans_list = ans_lists.pop()
        for i in range(len(ans_list)):
            node = ans_list[i]
            try:
                temp = [[] for _ in range(len(can_go[node]))]
                for i in range(len(can_go[node])):
                    if can_go[node][i] not in ans_list:
                        temp[i].extend(ans_list)
                        temp[i].append(can_go[node][i])
                for i in temp:
                    if len(i) > 0:
                        return_list.append(i)
                remove_list = []
                for i in return_list:
                    count = 1
                    for j in range(1, len(i)):
                        if info[i[j]] == 0:
                            count += 1
                        else:
                            count -= 1
                        if count < 1:
                            remove_list.append(i)
                    print("i:", i)
                    print("COUNT:", count > info.count(1))

            except:
                pass
        for remove_item in remove_list:
            return_list.remove(remove_item)
    return return_list


def count_sheep(info, key_list):
    count = 0
    for key in key_list:
        if info[key] == 0:
            count += 1
    return count


def solution(info, edges):
    edge_dict = {}
    if info.count(1) < 2:
        return info.count(0)
    cnt_list = [1]
    for i in range(len(info) - 1):
        edge_dict[edges[i][0]] = []
    edges = sorted(edges)
    for edge in edges:
        edge_dict[edge[0]].append(edge[1])
    t = get_com(edge_dict, info, [[0]])
    for i in range(len(info) - 1):
        t = get_com(edge_dict, info, t)
        temp = []
        for j in t:
            sheep_num = count_sheep(info, j)
            temp.append(sheep_num)
        try:
            cnt_list.append(max(temp))
        except:
            pass
    print(cnt_list)

    answer = 0
    return max(cnt_list)


test_edges = [[0, 1], [1, 2], [1, 4], [0, 8], [8, 7], [9, 10], [9, 11], [4, 3],
              [6, 5], [4, 6], [8, 9]]
test_info = [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]

print(solution(test_info, test_edges))
