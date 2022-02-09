import sys
N,K = map(int,(sys.stdin.readline().split()))
A = list()
count = 0
for i in range(N):
    A.append(int(sys.stdin.readline()))
A.reverse()
for j in range(len(A)):
    if K//A[j]>0:
        count += K//A[j]
        K = K-(A[j]*(K//A[j]))
    elif K==0:
        break
print(count)