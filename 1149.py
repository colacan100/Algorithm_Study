import sys
N = int(sys.stdin.readline())
color = list()
for i in range(N):
    color.append(list(map(int,sys.stdin.readline().split())))
for j in range(1,len(color)):
    color[j][0] = color[j][0] + min(color[j-1][1],color[j-1][2])
    color[j][1] = color[j][1] + min(color[j-1][0],color[j-1][2])
    color[j][2] = color[j][2] + min(color[j-1][0],color[j-1][1])
print(min(color[N-1][0],color[N-1][1],color[N-1][2]))