# 코드는 간단하지만 내용 이해가 좀 걸렸던 문제
import sys
N = int(sys.stdin.readline())
scale = list(map(int,sys.stdin.readline().split()))
scale.sort()
cnt = 0
for i in scale:
    if cnt+1 < i:
        break
    cnt += i
print(cnt+1)