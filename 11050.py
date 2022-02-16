import sys,math
N,K = map(int,sys.stdin.readline().split())
twohang = math.factorial(N)/(math.factorial(K)*math.factorial(N-K))
print(int(twohang))