import sys
N,K = map(int,sys.stdin.readline().split())
num_list = []
for i in range(1,N+1):
    num_list.append(i)
print('<', end='')
while num_list:
    for i in range(K-1):
        num_list.append(num_list[0])
        num_list.pop(0)
    print(num_list.pop(0), end='')
    if len(num_list)>0:
        print(', ', end='')
print('>')