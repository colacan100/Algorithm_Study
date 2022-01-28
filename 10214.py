T = int(input())
count_K,count_Y = 0,0
for i in range(T):
    for j in range(9):
        Y,K = map(int,input().split())
        count_Y +=Y
        count_K +=K
    if count_Y>count_K:
        print('Yonsei')
    elif count_Y<count_K:
        print('Korea')
    elif count_Y==count_K:
        print('Draw')