# 아직까지도 알고리즘을 봐야 흐름이 잡힌다.
# 익숙해질때까지 트라이
import sys
from collections import deque
# bfs
def bfs(n):
    queue = deque()
    queue.append(n)
    while queue:
        # queue에서 n빼냄
        n = queue.popleft()
        for i in graph[n]:
            # 다음 지역 방문 x일때
            if visited[i] == 0:
                # 숫자 1늘리고 queue에 넣어줌
                visited[i] = visited[n]+1
                queue.append(i)
# 모든 인원
all_num = int(sys.stdin.readline())
# 0 부터 모든 인원수까지 그래프
graph = [[] for _ in range(all_num+1)]
# 시작사람, 끝사람
hum1, hum2= map(int,sys.stdin.readline().split())
# 입력받을 관계수
chonsu_num = int(sys.stdin.readline())
# 관계입력받음
for _ in range(chonsu_num):
    x,y = map(int,sys.stdin.readline().split())
    # 그래프에 넣음
    graph[y].append(x)
    graph[x].append(y)
# 방문 여부
visited = [0]*(all_num+1)
bfs(hum1)
# 관계 없으면 -1
if visited[hum2] > 0:
    print(visited[hum2])
else:
    print(-1)