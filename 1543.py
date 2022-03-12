import sys
doc = sys.stdin.readline().strip()
word = sys.stdin.readline().strip()
i,cnt = 0,0
while i <= len(doc) - len(word):
    if doc[i:i + len(word)] == word:
        cnt += 1
        i += len(word)
    else:
        i+=1
print(cnt)