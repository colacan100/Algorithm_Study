A,B = map(int,input().split())
C = int(input())
minite1 = B+C
min_over = minite1//60
hour1 = A+min_over
hou_over = hour1//24
hour2 = hour1-hou_over*24
minite2 = minite1-min_over*60
print(hour2,minite2)