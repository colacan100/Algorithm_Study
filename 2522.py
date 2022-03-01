import sys
N = int(sys.stdin.readline())
star = '*'
blank = ' '
count = 1
for i in range(N):
    print(blank*(N-i-1) + star*count)
    count += 1
count -= 2
for j in range(1,N):
    print(blank*(j) + star*count)
    count -= 1