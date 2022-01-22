# 재귀함수 패턴
# list를 이용해보자
# 상당히 막혀서 자료를 좀 찾아봤다

N = int(input())     

def draw_star(n) :
    global Map # 전역변수
    
    if n == 3 :
        Map[0][:3] = Map[2][:3] = [1]*3 # 첫 번째 행, 세 번째 행 1
        # [1] * 3 = [1, 1, 1]
        Map[1][:3] = [1, 0, 1] # 두 번째 행 0
        return

    else:
        a = n//3
        draw_star(n//3)     # 재귀함수    
        for i in range(3) : # 행 3번반복
            for j in range(3) : # 열 3번반복
                if i == 1 and j == 1 : # 중복 제외
                    continue
                for k in range(a) :    # a*i+k행에서 a*j,a*j+1열까지 채움
                    Map[a*i+k][a*j:a*(j+1)] = Map[k][:a]    # 첫번째 패턴에서 복사해옴

# Map을 0으로 초기화
Map = [[0 for i in range(N)] for j in range(N)]

draw_star(N)

for i in Map :
    for j in i :
        if j==1 :
            print('*', end = '')
        else :
            print(' ', end = '')
    print()