M = int(input())
N = int(input())
sum=0
min=0
for n in reversed(range(M,N+1)):
    count = 0
    if n>1:
        for i in range(2,n):
            if n%i ==0:
                count += 1
        if count == 0:
            sum +=n
            min = n
if sum==0:
    print(-1)
else:
    print(sum)
    print(min)