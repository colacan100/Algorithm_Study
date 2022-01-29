# (이 나오면 stack에 넣음
# ()이 나오면 현재 스택에 있는 ( 수만큼 ans에 더함 
# )이 나오면 stack의 (를 pop하고 ans에 1을 더함
from sys import stdin
iron = stdin.readline().rstrip()
iron_list = list()
stack = list()
ans = 0
for j in iron:
    iron_list.append(j)
for i in range(len(iron_list)):
    if iron_list[i] == '(':
        stack.append('(')
    elif iron_list[i] == ')':
        if iron_list[i-1] =='(':
            stack.pop()
            ans += len(stack)
        elif iron_list[i-1] == ')':
            if len(stack)!=0:
                stack.pop()
                ans +=1        
print(ans)