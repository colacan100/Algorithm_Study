import sys
N,M = map(int,sys.stdin.readline().split())
list=[]
res = 0
for _ in range(M):
    pack,each = map(int,sys.stdin.readline().split())
    list.append([pack,each])
pack_list = sorted(list, key=lambda x : x[0])
each_list = sorted(list, key=lambda x : x[1])
# pack이 더 이득인 경우
if pack_list[0][0] <= each_list[0][1]*6:
    # pack을 사는게 남은 each 사는 것 보다 나은 경우
    if pack_list[0][0] < each_list[0][1] * (N % 6):
        res = pack_list[0][0] * ((N // 6)+1)
    else:
        res = pack_list[0][0] * (N // 6) + each_list[0][1] * (N % 6)
# each가 더 이득인 경우
else:
    res = each_list[0][1] * N
print(res)