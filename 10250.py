T = int(input())
for i in range(T):
    H,W,N = map(int,input().split()) #호텔의 층 수, 각 층의 방 수, 몇 번째 손님
    if N % H == 0:
        floor = H
        Ho = N//H
    else:
        floor = N%H
        Ho = N//H + 1
    print(floor*100+Ho)