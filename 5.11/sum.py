# 1789 수들의 합
# 4294967295=>1~10만까지의 합보다 작음

n = int(input())
print(((1 + n) * (n)) / 2)
ans = 0
temp = 1
while temp <= n:
    temp = ((1 + ans) * (ans)) / 2
    ans += 1
print(ans - 2)
