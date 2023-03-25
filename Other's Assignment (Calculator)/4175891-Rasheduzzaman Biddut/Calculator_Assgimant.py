


def AddTwoNumber(num1,num2):
    return num1 + num2

def SubTwoNumber(num1,num2):
    return num1 - num2

def MulTwoNumber(num1,num2):
    return num1 * num2

def DivTwoNumber(num1,num2):
    return num1 / num2

a = int(input("Enter a:"))
b = int(input("Enter b:"))

result = AddTwoNumber(a,a), SubTwoNumber(a,b), MulTwoNumber(a,b), DivTwoNumber(a,b)
print(result)
