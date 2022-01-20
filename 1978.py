N = int(input())
num = map(int,input().split())
sosu=0
for n in num:
    count = 0
    if n>1:
        for i in range(2,n):
            if n%i ==0:
                count += 1
        if count == 0:
            sosu +=1
print(sosu)