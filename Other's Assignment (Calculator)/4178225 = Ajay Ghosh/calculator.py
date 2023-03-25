def addtion(a, b):
    result = a + b
    return result

def subtraction(a, b):
    result = a - b
    return result

def multiplication(a, b):
    result = a * b
    return result

def division(a, b):
    result = a / b
    return result

print("Enter the operation ('/', '*', '+', '-': ")
operation = input()
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if operation == "+":
    calculation = addtion(num1, num2)
    print('The result is: ', calculation)
elif operation == "-":
    calculation = subtraction(num1, num2)
    print('The result is: ', calculation)
elif operation == "*":
    calculation = multiplication(num1, num2)
    print('The result is: ', calculation)
elif operation == "/":
    calculation = division(num1, num2)
    print('The result is: ', calculation)

else:
    print('Error')
