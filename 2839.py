N = int(input())
count = 0
while N>=0:
    if N%5==0:
        count += (N//5)
        print(count) 
        break
    N -= 3
    count += 1
else:
    print(-1)
# 처음에 문제를 잘못 이해했다. 5kg,3kg으로 정확히 나누어 떨어져야함