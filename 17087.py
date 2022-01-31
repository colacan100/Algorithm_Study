from sys import stdin
import math
N,S = map(int,stdin.readline().split())
A = list(map(int,stdin.readline().split()))
stack = list()
for i in A:
    stack.append(abs(i-S))
for j in range(len(stack)-1):
    stack[0] = math.gcd(stack[0],stack[1])
    stack.pop(1)
print(stack[0])