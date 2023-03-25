print('''
+ addition
- substraction
* multiplication
/ divide
''')
num = int(input("Enter the first value:"))
num_2 = int(input("Enter the second value:"))
opr = input("Enter the operator:")
if opr == "+":
    print(num+num_2)
elif opr =="-":
    print(num-num_2)
elif opr == "*":
    print(num*num_2)
elif opr == "/":
    print(num/num_2)
else:
    print("invalid syntax")



