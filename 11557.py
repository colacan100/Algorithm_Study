T = int(input())
max_drink = 0
max_school = ''
for i in range(T):
    N = int(input())
    for i in range(N):
        school,drink = input().split()
        if int(drink)>max_drink:
            max_drink = int(drink)
            max_school = school
    print(max_school)