from sys import stdin
while True:
    S = stdin.readline().rstrip('\n') # 공백을 다 없애버려서 초반에 오류
    up_count, down_count,num_count,blank_count = 0,0,0,0
    if not S:
        break
    for i in S:
        if i.isupper():
            up_count +=1
        elif i.islower():
            down_count +=1
        elif i.isdigit():
            num_count +=1
        elif i.isspace():
            blank_count+=1
    print(down_count, up_count, num_count, blank_count)