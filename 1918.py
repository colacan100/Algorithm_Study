from sys import stdin
sic = stdin.readline().rstrip()
stack_alpha = list()
stack = list()
for j in sic:
    if j.isupper():
        stack_alpha.append(j)
    else:
        if j == '(':
            stack_alpha.append(j)
        elif j=='*' or j=='/':
            while stack and (stack[-1]=='*' or stack[-1]=='/'):
                stack_alpha.append(stack.pop())
            stack_alpha.append(j)
        elif j=='+' or j=='-':
            while stack and stack[-1] != '(':
                stack_alpha.append(stack.pop())
            stack_alpha.append(j)
        elif j == ')':
            while stack and stack[-1] !='(':
                stack_alpha.append(stack.pop())
            stack_alpha.append(j)
### 하던거 나중에 마무리

