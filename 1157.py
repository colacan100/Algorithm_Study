x = input().upper()
dic = dict()
for i in x:
    dic[i] = dic.get(i,0) + 1
most = ''
max = 0
for j,k in dic.items():
    if max < k:
        max = k
        most = j
    elif max == k:
        most = '?'
print(most)