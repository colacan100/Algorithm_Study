import sys
import heapq

N,K = map(int,sys.stdin.readline().split())
gem = []
for _ in range(N):
    M,V = map(int,sys.stdin.readline().split())
    heapq.heappush(gem, [M, V])
bag = []
for _ in range(K):
    C = int(sys.stdin.readline().strip())
    heapq.heappush(bag, C)
cnt = 0
que = []
for _ in range(K):
    # bag의 수용량
    min_bag = heapq.heappop(bag)
    # bag의 수용량보다 작은 보석
    while gem and min_bag >= gem[0][0]:
        # 조건에 맞는 보석의 가격만 넣어준다
        [M, V] = heapq.heappop(gem)
        heapq.heappush(que, -V) # 최대힙을 만드는 방식
    # 남은 보석이 있는 경우
    if que:
        # 조건에 맞는 가장 비싼 보석 추가
        cnt -= heapq.heappop(que)
    # 남은 보석 없는 경우 (없어도 되지만 쓸데없는 반복줄임)
    elif not gem:
        break
print(cnt)