import sys
B,C,D= map(int,sys.stdin.readline().split())
burger= list(map(int,sys.stdin.readline().split()))
side= list(map(int,sys.stdin.readline().split()))
drink= list(map(int,sys.stdin.readline().split()))
burger.sort(reverse=True)
side.sort(reverse=True)
drink.sort(reverse=True)
set_num = min(B,C,D)
set_sale = sum(burger[0:set_num])*0.9 + sum(side[0:set_num])*0.9 + sum(drink[0:set_num])*0.9
set_no_sale = sum(burger[set_num:]) +sum(side[set_num:]) +sum(drink[set_num:])
print(sum(burger)+sum(side)+sum(drink))
print(int(set_sale+set_no_sale))