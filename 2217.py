import sys
N = int(sys.stdin.readline())
rope = list()
for _ in range(N):
    rope.append(int(sys.stdin.readline()))
rope.sort()
n_count = N
rope_list = list()
for i in range(N):
    rope_list.append(n_count*rope[i])
    n_count -= 1
print(max(rope_list))