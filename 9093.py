import sys
N = int(sys.stdin.readline())
for i in range(N):
    word = sys.stdin.readline().split()
    rev_word = []
    for i in word:
        for j in i:
            rev_word.append(j)
        for k in i:
            print(rev_word.pop(),end='')
        print(' ',end='')
    print('')