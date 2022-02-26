import sys
N = sys.stdin.readline().strip()
num_list = [0 for _ in range(10)]
for i in N:
    num_list[int(i)] += 1
num_list[6] += num_list[9]
num_list[9] = 0
if num_list[6] % 2 ==0:
    num_list[6] //= 2
else :
    num_list[6] = num_list[6]//2 + 1
print(max(num_list))