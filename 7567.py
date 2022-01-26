plate = input() + " "
count = 10
for i in range(len(plate)-1):
    if plate[i] == plate[i+1]:
        count += 5
    else:
        count += 10
print(count-10)