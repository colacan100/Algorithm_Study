#하노이의 탑
N = int(input())
'''
hanoi(3, A, C, B)
# N-1개의 원반을 A에서 B로
# N-1개의 원반을 B에서 C로
hanoi(2, A, B, C) # 2개의 원반을 B로, 1개의 원반을 C로 (경유)
hanoi(2, B, C, A) # B의 두개의 원반을 C로 (이 때 A경유)
'''
def hanoi(N, start, to, via): # N : 개수 Start: 출발점 to:도착점 via:경유점
    if N == 1:
        print(start, to)
    else:
        hanoi(N-1, start, via, to)
        print(start, to)
        hanoi(N-1, via, to, start)
print(2**N-1)
hanoi(N, 1, 3, 2)