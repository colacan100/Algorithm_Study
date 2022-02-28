# 문제를 이해하기 어려웠던 문제, 알고리즘을 찾아보니 내용은 생각보다 간단했다.
import sys
N,M = map(int,sys.stdin.readline().split())
A_list,B_list = [],[]
for _ in range(N):
    A_list.append(list(map(int,sys.stdin.readline().strip())))
for _ in range(N):
    B_list.append(list(map(int,sys.stdin.readline().strip())))
count = 0
# 변환함수
def convert(x, y):
    for row in range(x, x + 3):
        for col in range(y, y + 3):
            A_list[row][col] = 1 - A_list[row][col]        
# 가능한 행렬개수
for i in range(N - 2):
    for j in range(M - 2):
        if A_list[i][j] != B_list[i][j]:
            convert(i, j)
            count += 1
# A,B 일치여부 확인  
while True:
    for i in range(N):
        for j in range(M):
            if A_list[i][j] != B_list[i][j]:
                print(-1)
                exit(0)
    print(count)
    exit(0)