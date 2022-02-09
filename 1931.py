import sys
N = int(sys.stdin.readline())
Time = list()
for _ in range(N):
    Time.append(list(map(int,(sys.stdin.readline().split()))))
Time = sorted(Time, key=lambda x: x[0]) # 시작하는 시간 기준 오름차순 
Time = sorted(Time, key=lambda x: x[1]) # 끝나는 시간 기준 오름차순
Time_locate=0
count=0
for i,j in Time:
    if i >= Time_locate:
        count+=1
        Time_locate=j
print(count)