import sys
N = int(sys.stdin.readline())
star = '*'
blank = ' '
count = 2*N-1
for j in range(N):
    print(blank*(j) + star*count)
    count -= 2