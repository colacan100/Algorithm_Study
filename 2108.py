import sys
from collections import Counter
list_num = []
T = int(sys.stdin.readline())
for _ in range(T):
    list_num.append(int(sys.stdin.readline()))
list_num.sort()
mea = round(sum(list_num)/len(list_num))
mid = list_num[len(list_num)//2]
cnt = Counter(list_num).most_common(2)
if len(list_num) > 1:
    if cnt[0][1] == cnt[1][1]:
        bindo_num = cnt[1][0]
    else:
        bindo_num = cnt[0][0]
else:
    bindo_num = cnt[0][0]
road = max(list_num)-min(list_num)
print(mea)
print(mid)
print(bindo_num)
print(road)