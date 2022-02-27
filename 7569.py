import sys
from collections import deque
M,N,H = map(int,sys.stdin.readline().split())
dx = [-1,1,0,0,0,0]
dy = [0,0,-1,1,0,0]
dz = [0,0,0,0,-1,1]
graph = []
queue = deque()
for i in range(H):
    tmp = []
    for j in range(N):
        tmp.append(list(map(int,sys.stdin.readline().split())))
        for k in range(M):
            # tmp의 원소 중 1이면 큐에 추가
            if tmp[j][k] == 1:
                queue.append([i, j, k])
    # 3차원 배열 만듬
    graph.append(tmp)
while queue:
    # 이 부분에서 헷갈렸다. x가 높이 y가 세로 z가 가로를 의미한다.
    # 위의 for문에서 queue에 넣을 때 이 순서로 들어가기 때문
    x,y,z = queue.popleft()
    for i in range(6):
        nx = x + dx[i]
        ny = y + dy[i]
        nz = z + dz[i]
        # 따라서 여기서 nx에 H가 들어가는 것이다.
        if 0<=nx<H and 0<=ny<N and 0<=nz<M and graph[nx][ny][nz]==0:
            queue.append([nx,ny,nz])
            graph[nx][ny][nz] = graph[x][y][z]+1
cnt = 0
for i in graph:
    for j in i:
        for k in j:
            # bfs 지나도 0이면 토마토 못익음, -1, 프로그램 종료
            if k == 0:
                print(-1)
                exit(0)
        cnt = max(cnt, max(j))
# 시작지점 1이므로 -1 해야함
print(cnt-1)