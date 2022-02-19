# 알고리즘과 책을 참고했다.
# 계속 연습해봐야할 문제, 아무런 참고자료없이 구현할 수 있게 만들자.
import sys
from collections import deque

def dfs(n):
    print(n, end=' ')
    visited[n] = True
    for i in graph[n]:
        if not visited[i]:
            dfs(i)
def bfs(n):
    queue = deque([n])
    visited[n] = True
    while queue:
        v = queue.popleft()
        print(v, end= ' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

N,M,V = map(int,sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]
visited = [False] * (N + 1)
for _ in range(M):
    x,y = map(int,sys.stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x)
for i in range(1, N+1):
    graph[i].sort()
dfs(V)
visited = [False] * (N + 1)
print()
bfs(V)