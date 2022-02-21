# 그리디와 BFS를 이용해도 되는 문제였다.
# BFS 이용코드는 생각해내지 못했다. 노력이 더 필요하다.
'''BFS 이용코드
import sys
from collections import deque
a,b = map(int,sys.stdin.readline().split())
queue = deque([(a,1)])
res = -1
while queue:
    i, cnt = queue.popleft()
    if i == b:
        res = cnt
        break
    if i*2 <= b:
        queue.append((i*2,cnt+1))
    if int(str(i)+'1')<=b:
        queue.append((int(str(i)+'1'),cnt+1))
print(res)
'''
import sys
from collections import deque
a,b = map(int,sys.stdin.readline().split())
cnt = 1
while True:
    if b==a:
        break
    elif (b%2 !=0 and b%10 !=1) or (b<a):
        cnt = -1
        break
    else:
        if b%10 == 1:
            b//=10
            cnt+=1
        else:
            b//=2
            cnt+=1
print(cnt)