# 애매할 땐 경우의 수를 다 써보자
# 쉬울 줄 알았는데 생각보다 막혔던 문제
import sys
n = int(sys.stdin.readline())
podo = [0]
for _ in range(n):
    podo.append(int(sys.stdin.readline()))
dp = [0]
dp.append(podo[1])
if n>1:
    dp.append(podo[1]+podo[2])
    for i in range(3, n + 1):
        dp.append(max(dp[i-1],dp[i-3]+podo[i-1]+podo[i],dp[i-2]+podo[i]))
print(dp[n])