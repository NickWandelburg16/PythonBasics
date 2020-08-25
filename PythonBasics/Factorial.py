factorialValue = 5

def factorialOf(value):
    if value == 0:
        return 1
    else:
        return value * factorialOf(value - 1)

print("Factorial of ", factorialValue, " is: ", factorialOf(factorialValue))