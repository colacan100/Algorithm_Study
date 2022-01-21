def prime(num):
    if num==1:
        return False
    else:
        for i in range(2, int(num**0.5)+1):
            if num%i==0:
                return False
        return True

T = int(input())
for i in range(T):
    N = int(input())
    a = N/2
    b = N/2
    while True:
        if prime(a)==True and prime(b)==True:
            print(int(a),int(b))
            break
        else:
            a -= 1
            b += 1