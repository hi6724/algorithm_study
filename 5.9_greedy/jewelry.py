import sys
import heapq

N, K = map(int, sys.stdin.readline().split())
jew = []
for _ in range(N):
    heapq.heappush(jew, list(map(int, sys.stdin.readline().split())))
bags = []
for _ in range(K):
    bags.append(int(sys.stdin.readline()))
bags.sort()
print(bags)
answer = 0
tmp_jew = []
# bag 가벼운 순으로 탐색
# 첫번째 가방에 들어간다 => 다음가방에는 당연히 들어갈 수 있음
# 보석의 가치가 높은 순으로 하나 씩 꺼 내면 답
for bag in bags:
    while jew and bag >= jew[0][0]:
        heapq.heappush(tmp_jew, -heapq.heappop(jew)[1])
    if tmp_jew:
        answer -= heapq.heappop(tmp_jew)
    elif not jew:
        break

print(answer)