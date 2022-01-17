alphabet_list = ['c=','c-','dz=','d-','lj','nj','s=','z=']
x = input()
for i in alphabet_list:
    x = x.replace(i,'a')
print(len(list(x)))