a = int(input("Enter Your 1st Number: "))
b = int(input("Enter Your 2nd Number: "))


def divTwoNum(num1, num2):
    return num1 / num2


def addTwoNum(num1, num2):
    return num1 + num2


def subTwoNum(num1, num2):
    return num1 - num2


def mulTwoNum(num1, num2):
    return num1 * num2


def remainderTwoNum(num1, num2):
    return num1 % num2


def exponentTwoNum(num1, num2):
    return num1 ** num2


print("Here are the actions list:")
print("1. / (Division)")
print("2. + (Addition)")
print("3. - (Subtraction)")
print("4. * (Multiplication)")
print("5. % (Remainder)")
print("6. ** (Exponent)")

action = input("Now, enter the action you want: ")

if action == "/":
    print(divTwoNum(a, b))
elif action == "+":
    print(addTwoNum(a, b))
elif action == "-":
    print(subTwoNum(a, b))
elif action == "*":
    print(mulTwoNum(a, b))
elif action == "%":
    print(remainderTwoNum(a, b))
elif action == "**":
    print(exponentTwoNum(a, b))
else:
    print("Sorry, your action is not in our list")
