V = int(input())
num = input()
A_count = 0
B_count = 0
for i in num:
    if i == 'A' :
        A_count +=1
    elif i == 'B':
        B_count +=1
if A_count>B_count:
    print('A')
elif A_count<B_count:
    print('B')
elif A_count==B_count:
    print('Tie')