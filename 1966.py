# 알고리즘 일부 참고하였다.
# 문제에서 표현한 그대로 구현하도록 노력하자
import sys
T = int(sys.stdin.readline())
for i in range(T):
    N,M = map(int,sys.stdin.readline().split())
    imp = list(map(int,sys.stdin.readline().split()))
    imp_lst = [0 for _ in range(N)] 
    imp_lst[M] = 1
    cnt = 0
    while True:
        if imp[0] == max(imp):
            cnt += 1
            if imp_lst[0] != 1:
                del imp[0]
                del imp_lst[0]
            else:
                print(cnt)
                break
        else:
            imp.append(imp[0])
            del imp[0]
            imp_lst.append(imp_lst[0])
            del imp_lst[0]