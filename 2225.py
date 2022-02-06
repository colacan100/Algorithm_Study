import sys
N,K = map(int,sys.stdin.readline().split())
dp = [[0]*201 for _ in range(201)]
for i in range(1,N+1):
    if i == 1 :
        for j in range(1,K+1):
            dp[i][j] = j
    else:
        for j in range(1,K+1):
            dp[i][j] = (dp[i][j-1]+dp[i-1][j])
print(dp[N][K]%1000000000)