S = int(input())
count = 0
result = 0
while True:
    count +=1
    result += count
    if result > S:
        break
print(count-1)