N = int(input())
count = 2 
while N!=1:
    if N%count==0:
        N/=count
        print(count)
    else:
        count+=1