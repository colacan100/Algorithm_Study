import sys
N = int(sys.stdin.readline())
P = [0] + list(map(int,sys.stdin.readline().split()))
d = [0]*(N+1)
for i in range(1,N+1):
    d[i] = P[i]
    for j in range(1,i+1):
        if d[i-j] + P[j] < d[i]:
            d[i] = d[i-j] + P[j]
print(d[N])