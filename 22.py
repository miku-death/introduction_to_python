array1 = input().split()
array2 = input().split()

sortedArray = list(set(array1 + array2))
sortedArray = [int(x) for x in sortedArray]

sortedArray.sort()

print(sortedArray)
