from sys import stdin
S = stdin.readline().rstrip()
ans = ''
for i in S:
    if i.isupper() and i <= 'M':
        ROT = chr(ord(i)+13)
    elif i.isupper() and i > 'M':
        ROT = chr(ord(i)-13)
    elif i.islower() and i <= 'm':
        ROT = chr(ord(i)+13)
    elif i.islower() and i > 'm':
        ROT = chr(ord(i)-13)
    elif i.isspace:
        ROT = i
    ans += ROT
print(ans)