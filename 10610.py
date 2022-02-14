import sys
N = sys.stdin.readline().rstrip()
sort_n = sorted(N,reverse=True)
T = ''
for i in sort_n:
    T += i
if (int(T)%30) == 0:
    print(int(T))
else:
    print(-1)