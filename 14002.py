'''순서를 신경쓰지 못함, 역순으로 진행하면 해결
import sys
size = int(sys.stdin.readline())
A = list(map(int,sys.stdin.readline().split()))
dp = [0 for _ in range(size)]
for i in range(size):
    for j in range(i): 
        if A[i]>A[j] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] += 1
dp2 = list()
for k in range(1,max(dp)+1):
    dp2.append(A[dp.index(k)])
print(max(dp))
print(*dp2)
'''
import sys
size = int(sys.stdin.readline())
A = list(map(int,sys.stdin.readline().split()))
dp = [0 for _ in range(size)]
dp2 = list()
for i in range(size):
    for j in range(i): 
        if A[i]>A[j] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] += 1
count = max(dp)
for k in range(size-1,-1,-1):
    if dp[k] == count:
        dp2.append(A[k])
        count-=1
dp2.reverse()
print(max(dp))
print(*dp2)