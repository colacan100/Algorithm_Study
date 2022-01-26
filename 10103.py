n = int(input())
chang,sang = 100,100
for i in range(n):
    num1,num2 = map(int,input().split())
    if num1>num2:
        sang-=num1
    elif num1<num2:
        chang-=num2
print(chang)
print(sang)