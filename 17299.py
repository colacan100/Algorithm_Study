from sys import stdin
N = int(stdin.readline())
num = [i for i in map(int,stdin.readline().split())]
num_fre = dict()
for j in num:
    num_fre[j] = num_fre.get(j,0) + 1
stack = list()
answer =[-1] * N
for i in range(N):
    while stack and num_fre[num[stack[-1]]]<num_fre[num[i]]:
        answer[stack[-1]] = num[i]
        stack.pop()
    stack.append(i)
print(*answer)