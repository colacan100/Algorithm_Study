# 1931 회의실 문제와 비슷하지만 heap을 사용하여 해결해야한다.
# heap에 관한 알고리즘만 참고하였다.
import sys
import heapq
N = int(sys.stdin.readline())
Time = []
heap = []
for _ in range(N):
    S,T = map(int,sys.stdin.readline().split())
    Time.append([S,T])
Time = sorted(Time,key=lambda x:(x[0],x[1]))
heapq.heappush(heap,Time[0][1])
for i in range(1,N):
    if Time[i][0] < heap[0]:
        heapq.heappush(heap,Time[i][1])
    else:
        heapq.heappop(heap)
        heapq.heappush(heap,Time[i][1])
print(len(heap))
'''
틀렸다고 뜬 코드, 이유는 계속 찾아봐도 모르겠어서 질문 창에 올렸다.
import sys
N = int(sys.stdin.readline())
Time = []
heap = []
for _ in range(N):
    S,T = map(int,sys.stdin.readline().split())
    Time.append([S,T])
Time = sorted(Time,key=lambda x:(x[0],x[1]))
heap.append(Time[0][1])
for i in range(1,N):
    if Time[i][0] < heap[0]:
        heap.append(Time[i][1])
    else:
        heap.pop(0)
        heap.append(Time[i][1])
print(len(heap))
'''