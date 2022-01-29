'''시간초과 
from sys import stdin
N = int(stdin.readline())
num = [i for i in stdin.readline().split()]
nge = list()
new_num = list()
count = 0
for i in num:
    new_num = num[count+1:]
    count +=1
    if len(num)==count:
        nge.append('-1')
    for j in new_num:
        if i>max(new_num):
            nge.append('-1')
            break
        else:
            if i<j:
                nge.append(j)
                break
print(' '.join(nge))
'''
# 많이 막혔다. 추후 다시 복습할 것
from sys import stdin
N = int(stdin.readline())
num = [i for i in map(int,stdin.readline().split())]
stack = list()
answer =[-1] * N
for i in range(N):
    while stack and num[stack[-1]]<num[i]:
        # 오큰수를 구하지못하면 stack에 쌓아둠
        # 이후 오큰수를 구하면 stack에 쌓아둔 list도 동일 오큰수 
        answer[stack[-1]] = num[i]
        stack.pop()
    stack.append(i)
print(*answer) # *list : list 원소출력