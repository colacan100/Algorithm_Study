# 에라토스테네스의 체 이용
M,N = map(int,input().split())

def prime(num):
    if num==1:
        return False
    else:
        for i in range(2, int(num**0.5)+1): # 특정 숫자의 제곱근까지만 약수의 여부 검증 (더 빠름)
            if num%i==0:
                return False
        return True

for j in range(M,N+1):
    if prime(j)==True:
        print(j)