import sys
S = sys.stdin.readline().rstrip()
sum = 0
for i in range(len(S)-1):
    if S[i] != S[i+1]:
        sum +=1
print((sum+1)//2)