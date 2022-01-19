import math
A,B,V = map(int,input().split())
time = (V-A)/(A-B)
print(math.ceil(time)+1)
#시간초과에 유의하자