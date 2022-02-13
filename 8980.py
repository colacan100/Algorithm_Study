# 생각보다 어려웠던 문제, 알고리즘을 참고하여 풀었다.
import sys
N,C = map(int,sys.stdin.readline().split())
M = int(sys.stdin.readline())
opt = list()
for _ in range(M):
    opt.append(list(map(int,sys.stdin.readline().split())))
# 도착위치 중심 정렬
opt.sort(key=lambda x:x[1])
count = 0
# 각 위치에 남은 공간
locate = [C]*(N+1)  
for start,end,box in opt:
    min_box = C
    for i in range(start, end):
        min_box = min(min_box, locate[i])
    min_box = min(min_box, box)
    for i in range(start, end):
        locate[i] -= min_box
    count += min_box
print(count)