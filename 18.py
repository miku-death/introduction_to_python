from random import randint

arrayLength = int(input())
array = list()

for i in range(0, arrayLength):
    array.append(randint(0, arrayLength))

numberToCompare = int(input())
closestNumber = 0

for i in array:
    if i == numberToCompare:
        closestNumber = i
        break
    if abs(numberToCompare - i) < abs(numberToCompare - closestNumber):
        closestNumber = i

print(closestNumber)
