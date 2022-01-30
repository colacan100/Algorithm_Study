from sys import stdin
S = stdin.readline().rstrip()
stack = list()
for i in range(len(S)):
    stack.append(S[i:])
stack.sort()
for i in stack:
    print(i)