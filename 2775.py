T = int(input())
for i in range(T):
    floor = int(input())
    ho = int(input())
    f0 = [i for i in range(1,ho+1)] #list comprehension
    for j in range(floor):
        for i in range(1,ho):
            f0[i] += f0[i-1]
    print(f0[-1])