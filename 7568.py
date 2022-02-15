import sys
N = int(sys.stdin.readline())
num_lst = list()
rank = list()
for _ in range(N):
    num_lst.append(list(map(int,sys.stdin.readline().split())))
for i in range(N):
    count = 0
    for j in range(N):
        if num_lst[i][0] < num_lst[j][0] and num_lst[i][1] < num_lst[j][1]:
            count += 1
    rank.append(count+1)
print(*rank)