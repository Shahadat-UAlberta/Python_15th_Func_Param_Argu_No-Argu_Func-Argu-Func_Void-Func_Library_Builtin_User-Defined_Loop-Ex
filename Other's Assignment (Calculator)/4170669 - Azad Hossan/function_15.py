def add (num1, num2): 
    return num1 + num2 

def sub (num1, num2): 
    return num1 - num2 

def mul (num1, num2): 
    return num1 * num2

def div (num1, num2): 
    return num1 / num2 

a = float(input())
b = float(input())
operation = input('What do you want? +, -, * or /:--\n')

if operation == "+":
    print(add(a,b))
elif operation == "-":
    print(sub(a,b))
elif operation == "*":
    print(mul(a,b))
elif operation == "/":
    print(div(a,b))
else:
    print("not ok")
