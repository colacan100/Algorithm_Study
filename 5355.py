T = int(input())
for i in range(T):
    lst = []
    lst = input().split()
    count=float(lst[0])
    for i in lst:
        if i == '@':
            count*=3
        elif i == '%':
            count+=5
        elif i == '#':
            count-=7
    print('%0.2f' % count)