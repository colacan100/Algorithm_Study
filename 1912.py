import sys
size = int(sys.stdin.readline())
n = list(map(int,sys.stdin.readline().split()))
dp = list()
dp.append(n[0])
for i in range(1,len(n)):
    dp.append(max(dp[i-1]+n[i],n[i]))
print(max(dp))