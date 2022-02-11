import sys
T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    price = list(map(int, sys.stdin.readline().split()))
    total = 0
    for i in range(len(price)-1):
        count = price.pop(0)
        if max(price)-count>0:
            total+= max(price)-count
    print(total)