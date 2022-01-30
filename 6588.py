from sys import stdin
def prime(num):
    if num==1:
        return False
    else:
        for i in range(2, int(num**0.5)+1):
            if num%i==0:
                return False
        return True

while True:
    N = int(stdin.readline())
    if N==0:
        break
    a = N
    b = 0
    while True:
        if prime(a)==True and prime(b)==True:
            print(N,'=',int(b),'+',int(a))
            break
        else:
            a -= 1
            b += 1