import sys
N = int(sys.stdin.readline())
num = list(map(int,sys.stdin.readline().split()))
num2 = []
num2.append(num[0])
cnt = 1
for i in range(1,len(num)):
    if num[i]==0:
        num2.append(0)
    elif num[i-1] == 1 and num[i]==1:
        cnt+=1
        num2.append(cnt)
    else:
        cnt = 1
        num2.append(cnt)
print(sum(num2))