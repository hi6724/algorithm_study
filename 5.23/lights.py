repeat = int(input())
ans = []
for t in range(repeat):
    a, b, c, d = map(int, input().split())
    x = max(a, c)
    y = min(b, d)
    if y > x:
        ans.append(y - x)
    else:
        ans.append(0)
for a in range(len(ans)):
    print(f"#{a+1}", ans[a])
