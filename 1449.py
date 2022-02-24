import sys
N,L = map(int,sys.stdin.readline().split())
num_list = list(map(int,sys.stdin.readline().split()))
num_list.sort()
start = num_list[0]
end = num_list[0] + L - 0.5
cnt = 1
for i in range(N):
    if start <= num_list[i] < end:
        continue
    else:
        start = num_list[i]
        end = num_list[i] + L - 0.5
        cnt += 1
print(cnt)