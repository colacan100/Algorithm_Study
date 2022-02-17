import sys
N = int(sys.stdin.readline())
star = '*'
count = 1
for i in range(N):
    print(star*count)
    count += 1
count -= 2
for _ in range(N-1):
    print(star*count)
    count -= 1