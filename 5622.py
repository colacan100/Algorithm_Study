dial_list = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
x = input()
time = 0
for i in x:
    for j in dial_list:
        if i in j:
            time += dial_list.index(j) + 3
print(time)