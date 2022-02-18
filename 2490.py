import sys
N1 = list(map(int,sys.stdin.readline().split()))
N2 = list(map(int,sys.stdin.readline().split()))
N3 = list(map(int,sys.stdin.readline().split()))
def wood(x):
    if x==1:
        return print('A')
    elif x==2:
        return print('B')
    elif x==3:
        return print('C')
    elif x==4:
        return print('D')
    else:
        return print('E')
wood(N1.count(0))
wood(N2.count(0))
wood(N3.count(0))