import sys
N = int(sys.stdin.readline())
for i in range(N):
    VPS = sys.stdin.readline()
    VPS_lst = list(VPS)
    count = 0
    for i in VPS_lst:
        if i == '(':
            count+=1
        elif i == ')':
            count-=1
        if count<0:
            break
    if count==0:
        print('YES')
    else:
        print('NO')