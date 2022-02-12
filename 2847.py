import sys
T = int(sys.stdin.readline())
num_lst = list()
for _ in range(T):
    num_lst.append(int(sys.stdin.readline()))
count = 0
for i in range(len(num_lst)-1,0,-1):
    if num_lst[i-1]>=num_lst[i]:
        cha = num_lst[i-1]-num_lst[i]+1
        num_lst[i-1] -= cha
        count += cha
print(count)