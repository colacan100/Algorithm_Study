# 처음에 BFS라고 생각하지 않았다. 이런유형도 BFS임을 명심하자
import sys
from collections import deque
def bfs():
    queue = deque()
    queue.append(N)
    while queue:
        spot = queue.popleft()
        if spot==K:
            print(num[spot])
            break
        for i in (spot-1,spot+1,spot*2):
            if 0<=i<=100000 and num[i] == 0:
                num[i] = num[spot] + 1
                queue.append(i)
N,K = map(int,sys.stdin.readline().split())
num = [0] * (100001)
bfs()