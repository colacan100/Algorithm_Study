'''시간초과
import sys
N = int(sys.stdin.readline())
child = list(map(int,sys.stdin.readline().split()))
locate = list()
for i in range(1,len(child)+1):
    locate.append(child.index(i)+1)
count = 0
for j in range(len(locate)-1):
    if locate[j]>locate[j+1]:
        count += 1
print(count)
'''
import sys
N = int(sys.stdin.readline())
child = list(map(int,sys.stdin.readline().split()))
# 0 삽입하여 인덱스 맞춤
child.insert(0,0)
locate=[0]*(N+1)
for i in range(1,len(child)):
    locate[child[i]] = i
# 기본적으로 첫 값은 이동할 필요가 없음
count=1
max=0
for j in range(1,len(child)-1):
    # 이동할 필요가 없는 수
    if(locate[j] < locate[j+1]):
        count+=1
        if(count>max):
            max = count
    else:
        count=1
print(N-max)