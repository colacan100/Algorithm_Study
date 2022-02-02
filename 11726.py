import sys
# 다이나믹 프로그래밍의 경우 점화식을 찾을 것
# 점화식 d[N] = d[N-1]+d[N-2]
d = [0, 1, 2]
for i in range(3, 1001):
  d.append(d[i - 2] + d[i - 1])
n = int(sys.stdin.readline())
print(d[n] % 10007)