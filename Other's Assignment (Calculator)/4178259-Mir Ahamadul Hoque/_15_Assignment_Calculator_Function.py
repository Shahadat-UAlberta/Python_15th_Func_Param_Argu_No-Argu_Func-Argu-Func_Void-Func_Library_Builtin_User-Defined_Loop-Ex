
def sumResult(a,b) :
    return a + b
def multiplicationResult (a,b) :
    return a * b
def subtractResult (a,b) :
    return a - b
def divisionResult (a,b) :
    return a / b
import math
def sqrtResult (a) :
    result = math.sqrt(a)
    return result
def percentResult (a) :
    percent = "{:.0%}".format(a)
    return percent

num1 = 15
num2 = 10
num3 = 64

# SUMMATION
sum = sumResult (num1,num2)
print(sum)

# SUBTRACTION
subtract = subtractResult (num2,num1)
print(subtract)

# DIVISION
division = divisionResult(num1,num2)
print(division)

# MULTIPLICATION
multiply = multiplicationResult (num1,num2)
print(multiply)

# SQUARE ROOT
squareRoot = sqrtResult (num3)
print(squareRoot)

# PERCENTAGE
percentage = percentResult(division)
print(percentage)

