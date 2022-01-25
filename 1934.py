from math import gcd
T = int(input())
for i in range(T):
    A,B = map(int,input().split())
    print(int(A*B/gcd(A,B)))