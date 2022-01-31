from sys import stdin
import math
t = int(stdin.readline())
for i in range(t):
    stack = list(map(int,stdin.readline().split()))
    list_num = stack.pop(0)
    count = 0
    for j in range(list_num):
        for k in range(list_num):
            if j < k:
                count += math.gcd(stack[j],stack[k])
    print(count)