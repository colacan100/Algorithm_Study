import sys
N, B = sys.stdin.readline().split()
system = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
count = 0
for i in range(0,len(N)):
    index = system.find(N[len(N)-i-1])
    count += index*int(B)**i
print(count)