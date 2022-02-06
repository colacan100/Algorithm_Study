# 메모리 관리와 관련된 내용을 읽어보고 싶다.
# 교재가 도착하면 세부적으로 알아볼 예정
import sys
T = int(sys.stdin.readline())
dp = [0 for i in range(1000001)]
d = [0, 1, 2, 4]
for i in range(4, 1000001):
    d.append(d[i - 3]%1000000009 + d[i - 2]%1000000009 + d[i - 1]%1000000009)
for j in range(T):
    n = int(sys.stdin.readline())
    print(d[n] % 1000000009)