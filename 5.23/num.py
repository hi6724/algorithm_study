repeat = int(input())
for i in range(repeat):
    ans = "impossible"
    num = input()
    num_dict = {}
    for n in num:
        try:
            num_dict[n] += 1
        except:
            num_dict[n] = 1
    nums = []
    for j in range(2, 10):
        nums.append(int(num) * j)
    for j in nums:
        temp = {}
        for n in str(j):
            try:
                temp[n] += 1
            except:
                temp[n] = 1

        if temp == num_dict:
            ans = "possible"
    print(f"#{i+1} {ans}")
