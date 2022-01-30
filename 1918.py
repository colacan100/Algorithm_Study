from sys import stdin
sic = stdin.readline().rstrip()
stack = list()
ans = ''
for j in sic:
    if j.isupper():
        ans+=j
    else:
        if j == '(':
            stack.append(j)
        elif j=='*' or j=='/': # 우선순위가 낮은 +,- 출력
            while stack and (stack[-1]=='*' or stack[-1]=='/'):
                ans += stack.pop()
            stack.append(j)
        elif j=='+' or j=='-': # ( 나올때까지 출력
            while stack and stack[-1] != '(':
                ans += stack.pop()
            stack.append(j)
        elif j == ')': # ( 나올때까지 출력
            while stack and stack[-1] !='(':
                ans += stack.pop()
            stack.pop()
while stack:
    ans += stack.pop()
print(ans)