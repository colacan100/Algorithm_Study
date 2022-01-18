#1,7,19,37,61
bee = int(input())
bee_way = 1
count = 1
while bee>bee_way:
    bee_way += 6*count
    count+=1
print(count)