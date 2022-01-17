x,y = input().split()
a=list(x)
b=list(y)
a.reverse()
b.reverse()
revx = int(''.join(a)) #.join 리스트 합치기 함수
revy = int(''.join(b))
max = 0
if revx>revy:
    max = revx
elif revx==revy:
    max = revx
else:
    max = revy
print(max)