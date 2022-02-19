'''메모리초과
import sys
N = int(sys.stdin.readline())
num_lst = []
for _ in range(N):
    num_lst.append(int(sys.stdin.readline()))
num_lst.sort()
cnt = 0
for i in range(N-1):
    cnt += num_lst[i] + num_lst[i+1]
    num_lst[i+1] = cnt
print(cnt)
'''
import sys
import heapq
N = int(sys.stdin.readline())
num_lst = []
for _ in range(N):
    heapq.heappush(num_lst, int(sys.stdin.readline()))
cnt = 0
for i in range(N-1):
    temp1 = heapq.heappop(num_lst)
    temp2 = heapq.heappop(num_lst)
    cnt += temp1 + temp2
    heapq.heappush(num_lst, temp1 + temp2)
print(cnt)