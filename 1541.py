import sys
sic = sys.stdin.readline().split('-')
gwalho = list()
res = 0
for i in sic:
    count = 0
    sp_i = i.split('+')
    for j in sp_i:
        count += int(j)
    gwalho.append(count)
res += gwalho[0]
for k in range(1,len(gwalho)):
    res -= gwalho[k]
print(res)