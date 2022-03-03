import sys
N = int(sys.stdin.readline())
tree= list(map(int,sys.stdin.readline().split()))
tree.sort(reverse=True)
for i in range(len(tree)):
    # 심는 날 + 자라는 날
    tree[i] = tree[i] + i + 1
# 이장님 오는 날
print(max(tree)+1)