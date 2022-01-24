A,B,C = map(int,input().split())
D = int(input())
second1 = C+D
sec_over = second1//60
minite1 = B+sec_over
min_over = minite1//60
hour1 = A+min_over
hou_over = hour1//24
hour2 = hour1-hou_over*24
minite2 = minite1-min_over*60
second2 = second1-sec_over*60
print(hour2,minite2,second2)