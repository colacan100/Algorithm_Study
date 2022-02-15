'''부분성공
import sys
N = int(sys.stdin.readline())
road = list(map(int,sys.stdin.readline().split()))
oil = list(map(int,sys.stdin.readline().split()))
count = 0
count += road[0]*oil[0]
for i in range(1,N-1):
    count += road[i]*min(oil[0:i+1])
print(count)
'''
import sys
N = int(sys.stdin.readline())
road = list(map(int,sys.stdin.readline().split()))
oil = list(map(int,sys.stdin.readline().split()))
count = 0
cost = oil[0]
for i in range(N-1):
    if oil[i] < cost:
        cost = oil[i]
    count += road[i]*cost
print(count)