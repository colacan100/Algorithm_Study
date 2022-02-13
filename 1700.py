import sys
N,K = map(int,sys.stdin.readline().split())
multitap = list(map(int,sys.stdin.readline().split()))
plug = list()
count = 0
for i in range(K):
    # 이미 플러그에 있는 경우
    if multitap[i] in plug:
        continue
    # 플러그가 비어있는 경우
    if len(plug) < N:
        plug.append(multitap[i])
        continue
    # 플러그를 뽑아야하는 경우
    idx_lst = list()
    for j in range(N):
        # 플러그 꽂혀있는 전기용품이 이후에도 사용 O
        if plug[j] in multitap[i:]:
            idx = multitap[i:].index(plug[j])
        else:
            idx = 101
        # 플러그 꽂혀있는 전기용품이 이후에도 사용 X
        idx_lst.append(idx)
    # 사용 X or 가장 멀리 있는 index 지는 plug 제거
    plug_out = idx_lst.index(max(idx_lst))
    del plug[plug_out]
    plug.append(multitap[i])
    count +=1
print(count)