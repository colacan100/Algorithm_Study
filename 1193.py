x = int(input())
line = 0
while True:
    line += 1
    x -= line
    if x<=0:
        x += line
        line += 1
        break
if line%2==0:
    print(str(line-x)+'/'+str(x))
else:
    print(str(x)+'/'+str(line-x))
# line   1       2           3               4
#      (1/1),(1/2,2/1),(3/1,2/2,1/3),(1/4,2/3,3/2,4/1)
# 규칙성을 좀 더 생각해보자
