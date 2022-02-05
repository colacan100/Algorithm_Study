# dp문제의 대표문제라고 한다. 아직도 헤매는 중
import sys
size = int(sys.stdin.readline())
A = list(map(int,sys.stdin.readline().split()))
# 자신을 포함하여 만들수 있는 부분 수열 크기
dp = [0 for _ in range(size)]
for i in range(size):
    for j in range(i): 
        if A[i]>A[j] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] += 1
print(max(dp))