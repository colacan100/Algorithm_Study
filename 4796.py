import sys
count = 1
while True:
    L,P,V = map(int,sys.stdin.readline().split())
    if L==0 and P==0 and V==0:
        break
    res = L*(V//P)
    if V%P<L:
        res+=V%P
    else:
        res+=L
    print('Case %d: %d' %(count,res))
    count += 1