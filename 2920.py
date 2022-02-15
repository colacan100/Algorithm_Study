import sys
num = list(map(int,sys.stdin.readline().split()))
num_as = sorted(num)
num_de = sorted(num,reverse=True)
if num == num_as:
    print('ascending')
elif num == num_de:
    print('descending')
else :
    print('mixed')