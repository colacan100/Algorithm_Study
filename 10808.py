from sys import stdin
S = stdin.readline().rstrip()
num = {'a': 0,'b': 0,'c': 0,'d': 0,'e': 0,'f': 0,'g': 0,'h': 0,'i': 0,'j': 0,'k': 0,'l': 0,'m': 0,'n': 0,'o': 0,'p': 0,'q': 0,'r': 0,'s': 0,'t': 0,'u': 0,'v': 0,'w': 0,'x': 0,'y': 0,'z': 0}
stack = list()
for i in S:
    num[i] = num.get(i,0)+1
for j in range(26):
    stack.append(num[chr(j+97)])
print(*stack)