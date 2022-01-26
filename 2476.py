N = int(input())
count = list()
for i in range(N):
    A,B,C = map(int,input().split())
    if A==B and B==C:
        count.append(10000+A*1000)
    elif A==B and B!=C:
        count.append(1000+A*100)
    elif A==C and B!=C:
        count.append(1000+A*100)
    elif B==C and A!=C:
        count.append(1000+B*100)
    else:
        count.append(max(A,B,C)*100)
print(max(count))