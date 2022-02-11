'''틀린 코드
짜다가 이 방식은 모든 경우의 수를 고려하기 힘들다고 생각해서 멈춤.
또한 직관적이지도 못함.
import sys
T = int(sys.stdin.readline())
N_lst = list()
for _ in range(T):
    N_lst.append(int(sys.stdin.readline()))
N_lst.sort(reverse=True)
count = 0
while N_lst:
    if N_lst[0]==1 and N_lst[1]==1:
        count += N_lst[0] + N_lst[1]
        del N_lst[0]
        del N_lst[0]
    elif N_lst[0]>0 and N_lst[1]>0:
        count += N_lst[0]*N_lst[1]
        del N_lst[0]
        del N_lst[0]
    elif N_lst[0]==0 and N_lst[1]<0:
        del N_lst[0]
        del N_lst[0]
    else:
        count += N_lst[0]
        del N_lst[0]
print(count)
'''
# 수 묶기를 이용하는 것이 중요하다.
# 0,양수 = 덧셈
# 0,음수 = 곱셈
# 1,양수 = 덧셈
# 1,음수 = 덧셈 -> 따라서, 1 = 덧셈
# 양수,양수 = 곱셈
# 음수,음수 = 곱셈
# 양수,음수 = 덧셈
import sys
T = int(sys.stdin.readline())
pos  = []
neg = []
count = 0
for _ in range(T): # 양수,음수를 나누어 저장한다.
    N = int(sys.stdin.readline())
    if N > 1:
        pos.append(N)
    elif N == 1:
        count += 1
    else:
        neg.append(N)
pos.sort(reverse=True)
if len(pos) % 2 == 0: # 양수가 짝수개
    for i in range(0,len(pos),2):
        count += pos[i]*pos[i+1]
else: # 양수가 홀수개
    for j in range(0,len(pos)-1,2): 
        count += pos[j]*pos[j+1]
    count += pos[len(pos)-1]
neg.sort()
if len(neg) % 2 == 0: # 음수가 짝수개
    for k in range(0, len(neg), 2):
        count += neg[k]*neg[k+1]
else: # 음수가 홀수개
    for l in range(0, len(neg)-1, 2):
        count += neg[l]*neg[l+1]
    count += neg[len(neg)-1]
print(count)