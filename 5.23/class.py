repeat = int(input())

for rep in range(repeat):
    total = int(input())
    classes = list(map(int, input().split()))
    c_t = sum(classes)
    ans_list = []
    for i in range(7):
        ans = 0
        temp = classes[i:len(classes)] + classes[:i]
        ans += ((total // c_t) - 1) * 7
        temp_total = (c_t + total % c_t)
        index = 0
        print(temp)
        while temp_total > 0:
            ans += 1
            if temp[index] == 1:
                temp_total -= 1
            index = (index + 1) % 7
        ans_list.append(ans)
    print(f"#{rep+1} {min(ans_list)}")