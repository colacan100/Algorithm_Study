import sys
T = int(sys.stdin.readline())
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
def bfs(x, y):
    queue = [[x, y]]
    while queue:
        a,b = queue[0][0], queue[0][1]
        del queue[0]
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == 1:
                visited[nx][ny] = 0
                queue.append([nx,ny])
for i in range(T):
    M,N,K= map(int,sys.stdin.readline().split())
    visited = [[0]*M for _ in range(N)]
    cnt = 0
    for j in range(K):
        X, Y = map(int, input().split())
        visited[Y][X] = 1
    for ny in range(N):
        for nx in range(M):
            if visited[ny][nx]==1:
                bfs(ny,nx)
                visited[ny][nx]=0
                cnt+=1
    print(cnt)