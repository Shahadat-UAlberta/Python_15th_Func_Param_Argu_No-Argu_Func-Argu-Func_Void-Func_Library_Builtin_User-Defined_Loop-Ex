#_________________________ Calculator ________________________#
def add (num1, num2):
	return  num1 + num2
def sub (num1, num2) :
	return num1 - num2
def mul (num1, num2) :
	return num1 * num2
def div (num1, num2) :
	return num1 / num2
def rem (num1, num2):
	return num1 % num2


a = float(input("Inter First Number :- "))
b = float(input("Inter Second Number :- "))

operator = input("+ , - , * , /, // ")           # # % :-

if operator == "+":
	print(add(a, b))
elif operator == "-":
	print(sub(a, b))
elif operator == "*":
	print(mul(a, b))
elif operator == "/":
	print(div(a, b))
elif operator == "//":  # rem = //(Reminder)
	print(rem(a, b))
else:
	print("wrong operator")


