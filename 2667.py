import sys
N = int(sys.stdin.readline())
# 2차원 리스트 정보
graph = []
cnt = []
for _ in range(N):
    graph.append(list(map(int,sys.stdin.readline().strip())))
# 특정노드와 연결된 모든 노드 방문
def dfs(x,y):
    # 범위벗어나면 중지
    if x<0 or x>=N or y<0 or  y>=N:
        return False
    if graph[x][y] == 0:
        return False
    # 현재노드 방문 안한 경우
    global count
    count += 1
    # 방문처리
    graph[x][y] = 0
    # 재귀호출
    dfs(x-1,y)
    dfs(x,y-1)
    dfs(x+1,y)
    dfs(x,y+1)
    return True
count = 0
res = 0
for i in range(N):
    for j in range(N):
        if dfs(i,j) == True:
            cnt.append(count)
            res += 1
            count = 0
print(res)
cnt.sort()
for i in range(res):
    print(cnt[i])