from random import randint

numberToSearch = int(input())
count = 0

array = list()

for i in range(0, 100):
    array.append(randint(0, 20))
    print(array[i], end=" ")

print()

for i in array:
    if i == numberToSearch: count += 1

print(count)
