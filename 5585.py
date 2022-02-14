import sys
N = int(sys.stdin.readline())
coin = [500,100,50,10,5,1]
count = 0
money = 1000-N
for i in coin:
    count += money//i
    money = money % i
print(count)