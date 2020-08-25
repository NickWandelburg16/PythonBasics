min = 0
max = 10
stepSize = 1

evenNumbers = []
oddNumbers = []

for value in range(min, max, stepSize):
    if (value % 2 ) == 0:
        evenNumbers.append(value)
    else:
        oddNumbers.append(value)

print("Even Numbers: ", evenNumbers)
print("Odd Numbers: ", oddNumbers)

