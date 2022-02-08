# 이전 가장 긴 증가하는 부분 수열과 유사
import sys
size = int(sys.stdin.readline())
A = list(map(int,sys.stdin.readline().split()))
dp = [0 for _ in range(size)]
for i in range(size):
    for j in range(i): 
        if A[i]<A[j] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] += 1
print(max(dp))