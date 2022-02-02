# 규칙성 찾는 연습을 더 해보자
import sys
d = [0, 1, 3]
for i in range(3, 1001):
  d.append(2*d[i - 2] + d[i - 1])
n = int(sys.stdin.readline())
print(d[n] % 10007)