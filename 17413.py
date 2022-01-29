from sys import stdin
S = stdin.readline().rstrip()
tag = True
stack = ''
ans = ''
for i in S:
    if i == '<':
        tag = False
        ans += stack[::-1] # 처음부터 끝까지 역순으로 
        ans += i
        stack = ''
        continue
    elif i =='>':
        tag = True
        ans += i
        continue
    elif i == ' ':
        ans += stack[::-1]+i
        stack = '' 
        continue
    if tag==True:
        stack+=i  
    elif tag==False:
        ans+=i
print(ans+stack[::-1])