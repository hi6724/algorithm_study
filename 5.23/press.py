repeat = int(input())
for rep in range(repeat):
    n = int(input())
    nums = []
    for i in range(n):
        x, times = input().split()
        nums.append([x, int(times)])
    count = 1
    print(f"#{rep+1}")
    for num in nums:
        for i in range(num[1]):
            if count < 10:
                print(num[0], end='')
                count += 1
            else:
                print(num[0])
                count = 1
    print()