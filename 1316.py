num = int(input())
count=0
for i in range(num):
    word = input()
    for j in range(len(word)-1): #범위지정에 유의하자
        if word[j] != word[j+1]:
            if word[j] in word[j+1:]:
                count-=1
                break
    count+=1
print(count)