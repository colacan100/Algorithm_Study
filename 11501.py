'''시간초과
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
'''
import sys
T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    price = list(map(int,sys.stdin.readline().split()))
    total = 0
    for i in range(N-2,-1,-1):
        if price[i] > price[-1]: # 맨 뒤의 값이 작다면 update
            price[-1] = price[i]
        else:
            total += price[-1]-price[i] # 맨 뒤의 값이 크다면 total에 추가 (이득값)
    print(total)