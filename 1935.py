from sys import stdin
N = int(stdin.readline())
sic = stdin.readline().rstrip()
num_list = list()
stack = list()
for i in range(N):
    num_list.append(int(stdin.readline()))
for j in sic:
    if j.isupper():
        stack.append(num_list[ord(j)-65])
    else:
        str2 = stack.pop()
        str1 = stack.pop()
        if j == '+':
            stack.append(str1+str2)
        elif j == '-':
            stack.append(str1-str2)
        elif j == '*':
            stack.append(str1*str2)
        elif j == '/':
            stack.append(str1/str2)
print('%.2f' %stack[0])
