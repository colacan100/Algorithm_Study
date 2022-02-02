import sys
# A진법의 수를 m자리만큼 입력받아 B진법의 수로 표현
jin_a, jin_b = map(int,sys.stdin.readline().split())
m = int(sys.stdin.readline())
a_num = list(map(int,sys.stdin.readline().split()))
ten = 0
count = 0
for i in a_num[::-1]:
    ten += i*(jin_a**count)
    count +=1
ten_b_list = list()
while ten>0: 
    ten_b_list.append(str(ten % jin_b)) 
    ten //= jin_b
print(*ten_b_list[::-1])