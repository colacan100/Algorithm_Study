import sys
score = []
for i in range(5):
    score.append(sum(list(map(int,sys.stdin.readline().split()))))
print(score.index(max(score))+1, max(score))