import sys
N = int(sys.stdin.readline())
dp = [0, 3, 7]
for i in range(3, 100001):
    dp.append((dp[i - 2] + 2*dp[i - 1])%9901)
print(dp[N]%9901)