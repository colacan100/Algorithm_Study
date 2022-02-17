'''시간초과
import sys
T = int(sys.stdin.readline())
for _ in range(T):
    apply = list()
    N = int(sys.stdin.readline())
    for _ in range(N):
        apply.append(list(map(int,sys.stdin.readline().split())))
    apply = sorted(apply,key=lambda x:x[0],reverse=True)
    count = 0
    while len(apply)>1:
        if apply[0][0]>apply[1][0] or apply[0][1]>apply[1][1]:
            count += 1
            del apply[0]
        else:
            del apply[0]

    print(count)
'''
import sys
T = int(sys.stdin.readline())
for _ in range(T):
    apply = []
    N = int(sys.stdin.readline())
    for _ in range(N):
        apply.append(list(map(int,sys.stdin.readline().split())))
    apply = sorted(apply, key = lambda x : x[0])
    count = 1
    top = apply[0][1]
    for i in range(1,N):
        if top>apply[i][1]:
            count += 1
            top = apply[i][1]
    print(count)