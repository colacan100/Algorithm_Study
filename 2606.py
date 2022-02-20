# 아직까지는 적응을 하지 못한 느낌, 노력이 필요하다.
import sys
com = int(sys.stdin.readline())
ssang = int(sys.stdin.readline())
graph = [[]*com for _ in range(com+1)]
for _ in range(ssang):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
cnt = 0
visited = [False]*(com+1)
def dfs(x):
    global cnt
    visited[x] = True
    for i in graph[x]:
        if not visited[i]:
            dfs(i)
            cnt+=1
dfs(1)
print(cnt)