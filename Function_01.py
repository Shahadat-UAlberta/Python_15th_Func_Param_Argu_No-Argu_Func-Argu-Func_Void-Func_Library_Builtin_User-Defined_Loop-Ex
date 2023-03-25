def Add(num1, num2):
    return num1 + num2

def Sub(num1, num2):
    return num1 - num2

def Mul(num1, num2):
    return num1 * num2

def Div(num1, num2):
    return num1 / num2

def Per(num1, num2):
    return num1 % num2


a = int(input())
b = int(input())

result = Add(a, b), Sub(a, b), Mul(a, b), Div(a,b), Per(a,b)
print(result)