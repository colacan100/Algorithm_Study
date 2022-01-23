'''
# 시간초과 O(n)
import sys
Msg = sys.stdin.readline().strip()
N = int(sys.stdin.readline())
lst = list(Msg)
cursor = len(Msg)
for i in range(N):
    cmd = sys.stdin.readline().rstrip().split()
    if cmd[0] == 'L':
        if cursor !=0:
            cursor-=1
    elif cmd[0] == 'D':
        if cursor !=len(lst):
            cursor+=1
    elif cmd[0] == 'B':
        if cursor !=0:
            del lst[cursor-1]
            cursor-=1
    elif cmd[0] == 'P':
        plus = cmd[1]
        lst.insert(cursor,plus)
        cursor+=1
j=0
full = ''
while j < len(lst):
    full += lst[j]
    j += 1
print(full)
'''
# list 2개로 pop 이용
import sys
lst1 = list(sys.stdin.readline().strip())
lst2 = [] # 커서 기준 오른쪽
N = int(sys.stdin.readline())
n = len(lst1)
for i in range(N):
    cmd = sys.stdin.readline().strip()
    if cmd[0] == 'P':
        lst1.append(cmd[2])
    elif cmd[0] == 'L' and len(lst1)!=0:
        lst2.append(lst1.pop())
    elif cmd[0] == 'D' and len(lst2)!=0:
        lst1.append(lst2.pop())
    elif cmd[0] == 'B' and len(lst1)!=0:
        lst1.pop()
print(''.join(lst1+list(reversed(lst2))))