def Add(num1, num2) :
    return num1 + num2

def Sub(num1, num2):
    return num1 - num2

def Mul(num1, num2):
    return num1 * num2

def Div(num1, num2):
    return num1 / num2

def Per(num1, num2):
    return num1 % num2

def floor(num1, num2):
    return num1 // num2

def exponent(num1, num2):
    return num1 ** num2

a = int(input("Enter the first value:"))
b = int(input("Enter the second value:"))

result = Add(a, b), Sub(a, b), Mul(a, b), Div(a,b), Per(a,b),floor(a,b),exponent(a,b)
print(result)