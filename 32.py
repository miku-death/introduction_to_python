from random import randrange

a = int(input())
b = int(input())

array = []

for i in range(0, 10000):
    array.append(randrange(0, 1000))

indexes = list()

for i in range(0, len(array)):
    if array[i] <= b and array[i] >= a:
        indexes.append(i)
