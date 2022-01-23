#파이썬은 스택구조가 없으므로 list로 구현
import sys
N = int(sys.stdin.readline())
cmd_lst = []
for i in range(N):
    word = sys.stdin.readline().split() # input 이용할시 시간초과
    cmd = word[0]
    if cmd == 'push':
        cmd_lst.append(word[1])
    elif cmd == 'pop':
        if len(cmd_lst)==0:
            print(-1)
        else:
            print(cmd_lst.pop())
    elif cmd == 'size':
        print(len(cmd_lst))
    elif cmd == 'empty':
        if len(cmd_lst)==0:
            print(1)
        else:
            print(0)
    elif cmd == 'top':
        if len(cmd_lst)==0:
            print(-1)
        else:
            print(cmd_lst[-1])