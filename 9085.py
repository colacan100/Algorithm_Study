import sys
T = int(sys.stdin.readline())
for _ in range(T):
    int(sys.stdin.readline())
    N = list(map(int,sys.stdin.readline().split()))
    print(sum(N))