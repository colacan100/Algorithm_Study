# nCr = n!/(n-r)!r!
# 끝자리 0은 10의 배수
# 2의 개수, 5의 개수중 적은 것이 10의 개수
from sys import stdin
n,m = map(int,stdin.readline().rstrip().split())
def two(x):
    count = 0
    while x!=0:
        x = x//2
        count += x
    return count
def five(x):
    count = 0
    while x!=0:
        x = x//5
        count += x
    return count
print(min(two(n) - two(n - m) - two(m), five(n) - five(n - m) - five(m)))