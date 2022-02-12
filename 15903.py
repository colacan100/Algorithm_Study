import sys
n,m = map(int,sys.stdin.readline().split())
first = list(map(int,sys.stdin.readline().split()))
for i in range(m):
    first.sort()
    temp = first[0]+first[1]
    first[0] = temp
    first[1] = temp
print(sum(first))