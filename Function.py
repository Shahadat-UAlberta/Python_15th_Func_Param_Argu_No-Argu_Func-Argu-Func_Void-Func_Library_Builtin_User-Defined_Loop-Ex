# Parameters / Argument
# No Argument Function and Argument Function
# Void Function
# Library / Builtin Function
# User Defined Function

def getMaxNum(num1, num2):
    if num1 > num2:
        return num1
    elif num2 > num1:
        return num2


def getMinNum(num1, num2):
    if num1 < num2:
        return num1
    elif num2 < num1:
        return num2


# Void Function
def printMessage():
    print("Hello World!")


def divTwoNum(num1, num2):
    return num1 / num2


a = 100
b = 20
result = getMaxNum(a, b)
print(result)

a = 200
b = 300
result2 = getMaxNum(a, b)
print(result2)

msg = printMessage()
print(msg)

# Add
# Sub
# Mul
# Div
