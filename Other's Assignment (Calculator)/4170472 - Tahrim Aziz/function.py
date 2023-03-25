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

num1 = 10
num2 = 20
num3 = 30


sum = sumResult (num1,num2)
print(sum)


subtract = subtractResult (num2,num1)
print(subtract)


division = divisionResult(num1,num2)
print(division)


multiply = multiplicationResult (num1,num2)
print(multiply)


squareRoot = sqrtResult (num3)
print(squareRoot)


percentage = percentResult(division)
print(percentage)
