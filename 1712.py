A,B,C = map(int,input().split()) # map함수: 리스트 요소를 지정함수로 처리
if B>=C:
    print(-1)
else: print(int(A/(C-B))+1)