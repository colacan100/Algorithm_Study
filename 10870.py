#재귀함수 이용할 것
n = int(input())
def Fibo(x):
    if x==0:
        return 0
    elif x==1:
        return 1
    return Fibo(x-1)+Fibo(x-2)
print(Fibo(n))