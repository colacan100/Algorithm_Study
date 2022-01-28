from sys import stdin
N = int(stdin.readline())
Deque =[]
for i in range(N):
    cmd = stdin.readline().split()
    if cmd[0]=='push_front':
        Deque.insert(0,cmd[1])
    elif cmd[0]=='push_back':
        Deque.insert(len(Deque),cmd[1])
    elif cmd[0]=='pop_front':
        if len(Deque)!=0:
            print(Deque.pop(0))
        else:
            print(-1)
    elif cmd[0]=='pop_back':
        if len(Deque)!=0:
            print(Deque.pop(-1))
        else:
            print(-1)
    elif cmd[0]=='size':
        print(len(Deque))
    elif cmd[0]=='empty':
        if len(Deque) == 0:
            print(1)
        else:
            print(0)
    elif cmd[0]=='front':
        if len(Deque)!=0:
            print(Deque[0])
        else:
            print(-1)
    elif cmd[0]=='back':
        if len(Deque)!=0:
            print(Deque[-1])
        else:
            print(-1)