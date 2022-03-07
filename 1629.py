# 단순히 생각했다가 한번 틀렸다. 시간초과를 간과하지말자.
import sys
def Division(a, b):
    if b==1:
        return a%C
    else:
        num = Division(a,b//2)
        if b%2 == 0:
            return num*num%C
        else:
            return num*num*a%C
A,B,C= map(int,sys.stdin.readline().split())
print(Division(A,B))