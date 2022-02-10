import sys
N = int(sys.stdin.readline())
A = list(map(int,(sys.stdin.readline().split())))
B = list(map(int,(sys.stdin.readline().split())))
count = 0
for i in range(N):
    count += min(A) * max(B)
    A.pop(A.index(min(A)))
    B.pop(B.index(max(B)))
print(count)