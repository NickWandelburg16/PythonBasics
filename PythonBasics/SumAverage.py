min = 1
max = 10
stepSize = 1

numElements = 0
sum = 0

for value in range(min, max, stepSize):
    sum += value
    numElements += 1

average = (1/numElements)*sum

print("Sum: ", sum)
print("Average: ", average)
