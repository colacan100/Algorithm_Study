# 이해하는데 오래걸림, 두 개의 list를 통해서 규칙성을 얻는 새로운 유형
#d[1] = d[0] + p[1]
#d[2] = d[1] + p[1] or d[0] + p[2]
#d[3] = d[2] + p[1] or d[1] + p[2] or d[0] + p[3]
#d[4] = d[3] + p[1] or d[2] + p[2] or d[1] + p[3] or d[0] + p[4]
import sys
N = int(sys.stdin.readline())
P = [0] + list(map(int,sys.stdin.readline().split()))
d = [0]*(N+1)
for i in range(1,N+1):
    for j in range(1,i+1):
        if d[i-j] + P[j] > d[i]:
            d[i] = d[i-j] + P[j]
print(d[N])