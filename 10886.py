N = int(input())
count_cute = 0
count_nocute = 0
for i in range(N):
    cute = int(input())
    if cute==1:
        count_cute +=1
    elif cute==0:
        count_nocute +=1
if count_cute>count_nocute:
    print('Junhee is cute!')
elif count_cute<count_nocute:
    print('Junhee is not cute!')