# 문제 이해하는데 시간이 좀 걸렸다. 더 체계적으로 생각해보자
import sys
N = int(sys.stdin.readline())
stack = []
num_lst = []
pp_lst = []
pos = True
count = 1
for i in range(N):
    num = int(sys.stdin.readline())
    while count<=num:
        stack.append(count)
        pp_lst.append('+')
        count+=1
    if stack[-1] == num:
        stack.pop()
        pp_lst.append('-')
    else:
        print('NO')
        pos = False
        break
if pos==True:
    for i in pp_lst:
        print(i)