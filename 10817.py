A,B,C = map(int,input().split())
result_max = max(A,B,C)
if A==result_max:
    if B>C:
        result = B
    else:
        result = C
if B==result_max:
    if A>C:
        result = A
    else:
        result = C
if C==result_max:
    if A>B:
        result = A
    else:
        result = B        
print(result)