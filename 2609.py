import math
num1,num2 = map(int,input().split())
ans1 = math.gcd(num1,num2)
ans2 = int(num1*num2/ans1)
print(ans1)
print(ans2)