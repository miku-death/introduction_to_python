bushes = input().split()
bushes = [int(x) for x in bushes]

print(bushes)

maxSum = 0

for i in range(1, len(bushes) - 1):
    localSum = bushes[i-1] + bushes[i] + bushes[i+1]
    maxSum = max(localSum, maxSum)

maxSum = max(maxSum, bushes[0] + bushes[1] + bushes[len(bushes) - 1])
maxSum = max(maxSum, bushes[len(bushes) - 1] + bushes[len(bushes) - 2] + bushes[0])

print(maxSum)
