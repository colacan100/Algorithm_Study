import sys
N = int(sys.stdin.readline())
pibo = list(0 for _ in range(N+1))
pibo[0] = 0
pibo[1] = 1
for i in range(2,N+1):
    pibo[i] = pibo[i-1]+pibo[i-2]
print(pibo[N])