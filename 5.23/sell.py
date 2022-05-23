# 메모리초과

repeat = int(input())
for i in range(repeat):
    n = int(input())
    prices = list(map(int, input().split()))
    sorted_prices = sorted(prices, reverse=True)
    sorted_dict = {}
    for p in sorted_prices:
        try:
            sorted_dict[p] += 1
        except:
            sorted_dict[p] = 1
    buy = []
    ans = 0
    for price in prices:
        for key, value in sorted_dict.items():
            temp = key
            break
        if price < temp:
            buy.append(price)
        else:
            for item in buy:
                ans += (price - item)
                sorted_dict[item] -= 1
                if sorted_dict[item] == 0:
                    sorted_dict.pop(item)
            buy = []
            sorted_dict[price] -= 1
            if sorted_dict[price] == 0:
                sorted_dict.pop(price)
    print(f"#{i+1}", ans)

# 뒤에서 부터 비교하면 됨
T = int(input())
for t in range(1, T + 1):
    num = int(input())
    arr = list(map(int, input().split()))
    last = arr[-1]
    cnt = 0
    for i in range(len(arr) - 1, -1, -1):  # 핵심! 뒤부터 보기
        if last > arr[i]:
            cnt += last - arr[i]
        else:  # 같거나 작을 때
            last = arr[i]
    print("#{} {}".format(t, cnt))