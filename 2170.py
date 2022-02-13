import sys
T = int(sys.stdin.readline())
num_lst = list()
for _ in range(T):
    num_lst.append(list(map(int,sys.stdin.readline().split())))
num_lst = sorted(num_lst,key=lambda x:(x[0],x[1]))
min_num = num_lst[0][0]
max_num = num_lst[0][1]
count = 0
for i in range(1,T):
    if max_num < num_lst[i][0] :
        count += (max_num-min_num)
        min_num = num_lst[i][0]
        max_num = num_lst[i][1]
    elif max_num < num_lst[i][1] :
        max_num = num_lst[i][1]
count += (max_num-min_num)
print(count)