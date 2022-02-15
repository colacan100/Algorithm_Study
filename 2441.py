import sys
N = int(sys.stdin.readline())
star = '*'
blank = ' '
for i in range(N,0,-1):
    print(blank*(N-i) + star*i)