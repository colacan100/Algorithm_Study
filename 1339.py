import sys
N = int(sys.stdin.readline())
word_list = []
dic={}
for _ in range(N):
    word_list.append(sys.stdin.readline().strip())

for alpha in word_list:
    cnt = len(alpha)
    for i in alpha:
        if i not in dic:
            dic[i] = (10**(cnt-1))
        else:
            dic[i] += (10**(cnt-1))
        cnt-=1
dic_val = list(dic.values())
dic_val.sort(reverse=True)
res = 0
num = 9
for i in dic_val:
    res += i*num
    num-=1
print(res)