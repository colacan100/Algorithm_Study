'''
#시간초과코드
while True:
    N = int(input())
    if N==0:
        break
    else:
        count=0
        for i in range(N+1,2*N+1):
            if i==1:
                continue
            elif i==2:
                count +=1
                continue
            else:
                for j in range(2, int(i**0.5)+1): #for else문 을 사용하였다.
                    if i%j==0:
                        break
                else:
                    count+=1
        print(count)
'''
def prime(num):
    if num==1:
        return False
    else:
        for i in range(2, int(num**0.5)+1):
            if num%i==0:
                return False
        return True

lst = list(range(2,246912)) # 배열을 미리 만들어 놓는다
prime_lst = [] # 소수만 모아놓은 배열
for i in lst:
    if prime(i):
        prime_lst.append(i)

while True:
    N = int(input())
    if N==0:
        break
    else:
        count = 0
        for j in prime_lst:
            if N< j <=N*2:
                count+=1
        print(count)