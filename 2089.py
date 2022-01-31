import sys
N = int(sys.stdin.readline())
count = ''
if N==0:    # 예외처리 확실히하자
    print(0)
else:
    while N:
        if N%(-2) != 0:
            count = '1' + count
            N = N//-2+1
        else:
            count = '0' + count
            N //= -2
        if(N==0):
            break
print(count)