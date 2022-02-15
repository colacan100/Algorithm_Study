import sys
N = list(map(int,sys.stdin.readline().split()))
for i in range(len(N)):
    N[i] = N[i]**2
print(sum(N)%10)