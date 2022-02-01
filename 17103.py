'''시간초과
from sys import stdin
def prime(num):
    if num == 1 or num == 0:
        return False
    else:
        for i in range(2, int(num ** 0.5)+1):
            if num % i == 0:
                return False
        return True
prime_list = [prime(i) for i in range(1000001)]
T = int(stdin.readline())
for j in range(T):
    N = int(stdin.readline())
    count = 0
    for k in range(N//2+1):
        if prime_list[k]==True and prime_list[N-k]==True:
            count+=1
    print(count)
'''

import sys
T = int(sys.stdin.readline())
prime = [True for i in range(1000001)] 
# 전체 리스트를 만들고 확인하는 방식이 효율적
prime[0] = prime[1] = False
for i in range(2, 1001):
    for j in range(i*2, 1000001, i):
        prime[j] = False
for i in range(T):
    count = 0
    N = int(sys.stdin.readline())
    for j in range(2,int(N/2)+1):
        if prime[j] and prime[N-j]:
            count += 1 
    print(count)