# 점화식은 알고리즘을 참고했다.
# dp[i] = min(dp[i - j]) + 1
# 아직까지 패턴 파악에 걸리는 시간이 오락가락하다.
import sys
N = int(sys.stdin.readline())
dp = [0 for _ in range(N + 1)]
square = [k*k for k in range(1, 317)]
for i in range(1,N+1):
    count = list()
    for j in square:
        if j>i:
            break
        count.append(dp[i - j])
    dp[i] = min(count) + 1
print(dp[N])