repeat = int(input())

for rep in range(repeat):
    ans = 0
    n, l = map(int, input().split())
    l = l * 2 + 1
    ans = (n // l) + 1
    if n % l == 0:
        ans -= 1

    print(f"#{rep+1} {ans}")
