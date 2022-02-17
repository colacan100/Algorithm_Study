import sys
N = int(sys.stdin.readline())
star = '*'
blank = ' '
count = 1
for i in range(N):
    print(star*count + blank*2*(N-i-1) + star*count)
    count += 1
count -= 2
for i in range(N-1):
    print(star*count + blank*2*(i+1) + star*count)
    count -= 1