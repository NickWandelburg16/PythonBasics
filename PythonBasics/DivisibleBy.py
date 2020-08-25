divisibleBy = [7,5]
devisibleValues = []

def divisbleBy(value):
    for divisor in divisibleBy:
        if not (value % divisor) == 0:
            return
    devisibleValues.append(value)

for value in range(1500, 2701):
    divisbleBy(value)

print(devisibleValues)
