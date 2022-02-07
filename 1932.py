import sys
T = int(sys.stdin.readline())
dp = list()
for _ in range(T):
    dp.append(list(map(int,(sys.stdin.readline().split()))))
count=2
for i in range(1, T):
    for j in range(count):
        # 행의 양쪽 끝은 그냥 더함
        if j==0:
            dp[i][j]=dp[i-1][j]+dp[i][j]
        elif i==j:
            dp[i][j]=dp[i-1][j-1]+dp[i][j]
        # 이전 행의 왼쪽과 오른쪽 중 큰 값
        else:
            dp[i][j]=max(dp[i-1][j-1],dp[i-1][j])+dp[i][j]
    count+=1
print(max(dp[T-1]))