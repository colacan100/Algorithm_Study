#재귀함수를 이용할 것
N = int(input())
def factor(x):
    if x<1:
        return 1
    return x*factor(x-1)
    
if N==0 :
    print(1)
else:
    print(factor(N))