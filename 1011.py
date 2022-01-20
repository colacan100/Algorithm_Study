import math
T = int(input())
for i in range(T):
    x,y = map(int,input().split())
    togo = y-x
    count = 0
    num = math.floor(math.sqrt(togo)) # root 및 내림
    if togo<4:
        count = togo
    elif togo>num**2+num:
        count = 2*num+1
    elif num**2<togo<=num**2+num:
        count = 2*num
    elif togo == num**2:
        count = 2*num-1
    print(count)
'''
togo count
1      1      1
2      2      11
3      3      111
4      3      121 root4까지 갔다옴 ) -1~0까지 count3, 1~2까지 count4, 3~4까지 count5 
5      4      1211
6      4      1221
7      5      12211
8      5      12221
9      5      12321 root9까지 갔다옴 ) -1~0까지 count5, 1~3까지 count6,4~5까지 count7
10     6      123211
11     6      123221
12     6      123321
13     7      1233211
14     7      1233221
15     7      1233321
16     7      1234321 root16까지 갔다옴 )-1~0까지 count7, 1~4까지 count8,5~6까지 count9
'''
# 규칙성 찾는 것이 중요했다