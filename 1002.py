T = int(input())
for i in range(T):
    x1,y1,r1,x2,y2,r2 = map(int,input().split())
    total_len = ((x1-x2)**2 + (y1-y2)**2)**(1/2)

    if total_len == 0 and r1 == r2: # 동심원
        print(-1)
    elif abs(r1-r2) == total_len or r1+r2 == total_len: # 내접, 외접
        print(1)
    elif abs(r1-r2) < total_len < r1+r2 :
        print(2)
    else:
        print(0)