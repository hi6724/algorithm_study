repeat = int(input())

for rep in range(repeat):
    n = int(input())
    arr = []
    for i in range(n):
        arr.append(list(input()))
    ans = []
    for i in range(n):
        for j in range(n):
            if arr[i][j] == "#":
                ans.append([i, j])
    first = ans[0]
    last = []
    for i in ans:
        if i[0] != first[0]:
            break
        last = i
    height = [first[1], last[1]]
    width = [first[0], first[0] + (last[1] - first[1])]
    temp_w = []
    temp_h = []
    temp = []

    for i in range(width[0], width[-1] + 1):
        temp_w.append(i)
    for i in range(height[0], height[-1] + 1):
        temp_h.append(i)
    if len(temp_h) != len(temp_w):
        print(f"#{rep+1} no")
        continue
    for i in temp_w:
        for j in temp_h:
            temp.append([i, j])
    print(temp)
    if temp == ans:
        print(f"#{rep+1} yes")
    else:
        print(f"#{rep+1} no")
