import sys
n = int(sys.stdin.readline())
array= list((map(int,(sys.stdin.readline().split()))))
dp = list(x for x in array)
dp[0] = array[0]
for i in range(1,n):
    for j in range(i):
        if array[j]<array[i]:
            dp[i]=max(dp[i],dp[j]+array[i])
print(max(dp))