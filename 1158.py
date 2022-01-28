from sys import stdin
N,K = map(int,stdin.readline().split())
N_list = list()
K_list = list()
count = 0
for i in range(1,N+1):
    N_list.append(i)
for j in range(N):
    count += K-1
    if count >= len(N_list):
        count = count%len(N_list)
    K_list.append(str(N_list.pop(count))) # join으로 리스트 불러옴
print('<'+', '.join(K_list)+'>')