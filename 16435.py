import sys
N,L = map(int,sys.stdin.readline().split())
snakebird= list(map(int,sys.stdin.readline().split()))
snakebird.sort()
for i in snakebird:
    if L>=i:
        L+=1
print(L)