import sys
N,M= map(int,sys.stdin.readline().split())
# 이동불가
if N == 1:
    print(1)
# 2번과 3번만을 사용하는 것이 최댓값
elif N == 2:
    print(min(4,((M+1)//2)))
# 1번과 4번만을 사용하는 것이 최댓값
elif M<=6:
    print(min(4,M))
else:
    print(M-2)