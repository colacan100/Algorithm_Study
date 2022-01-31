from sys import stdin
N = stdin.readline()
ten = int(N,2)
eight=str(oct(int(ten)))
print(int(eight[2:]))