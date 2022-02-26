import sys
num = []
a1,b1 = map(int,sys.stdin.readline().split())
a2,b2 = map(int,sys.stdin.readline().split())
a3,b3 = map(int,sys.stdin.readline().split())
a4,b4 = map(int,sys.stdin.readline().split())
num1 = b1-a1
num.append(num1)
num2 = num1-a2+b2
num.append(num2)
num3 = num2-a3+b3
num.append(num3)
num4 = num3-a4+b4
num.append(num4)
print(max(num))