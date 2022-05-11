# 문자 재정렬 연습문제
n = input()
number = 0
ans = ''
for i in range(len(n)):
    try:
        number += int(n[i])
    except:
        ans += n[i]
ans = sorted(ans)
ans = ''.join(str(s) for s in ans)
print(ans + str(number))
