import sys
N = int(sys.stdin.readline())
star = '*'
blank = ' '
count = 1+2*(N-1)
for i in range(N-1):
    print(blank*(i)+ star*count)
    count -= 2
count = 1
for i in range(N):
    print(blank*(N-i-1)+ star*count)
    count += 2