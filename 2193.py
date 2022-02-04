import sys
dp = [1,1]
N = int(sys.stdin.readline())
for i in range(2, 91):
    dp.append(dp[i-2]+dp[i-1])
print(dp[N-1])