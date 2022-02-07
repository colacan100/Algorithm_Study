import sys
T = int(sys.stdin.readline())
for _ in range(T):
    n = int(sys.stdin.readline())
    dp = list()
    dp.append(list(map(int,sys.stdin.readline().split())))
    dp.append(list(map(int,sys.stdin.readline().split())))
    for i in range(1,n):
        if i==1:
            dp[0][i] = dp[0][i] + dp[1][i-1]
            dp[1][i] = dp[i][1] + dp[0][i-1]
        else:
            dp[0][i] = max(dp[1][i-2],dp[1][i-1])+dp[0][i]
            dp[1][i] = max(dp[0][i-2],dp[0][i-1])+dp[1][i]
    print(max(dp[0][n-1],dp[1][n-1]))