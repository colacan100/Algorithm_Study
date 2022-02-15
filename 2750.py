import sys
N = int(sys.stdin.readline())
num_list = []
for _ in range(N):
    num = int(sys.stdin.readline())
    num_list.append(num)
num_list.sort()
for i in num_list:
    print(i)