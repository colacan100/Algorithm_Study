import math
pallin = input()
count = 0
for i in range(int(math.ceil((len(pallin)-1)/2))):
    if pallin[i]==pallin[len(pallin)-i-1]:
        count+=1
if count == int(math.ceil((len(pallin)-1)/2)):
    print(1)
else:
    print(0)