
print("==================Calculator With Function: =============")
def calculator(a,b,c):
    if ope=="+":
        return num1+num2
    elif ope=="-":
        return num1-num2
    elif ope=="*":
        return num1*num2
    elif ope=="/":
        return num1/num2
    elif ope=="%":
        return num1%num2
    elif ope=="//":
        print(num1//num2)
    elif ope=="**":
        print(num1**num2)
    else:
        print("Enter wrong.Please try again.Thanks:")


num1=int(input("Enter first number: "))
ope=input("Enter operator: ")
num2=int(input("Ener second number: "))

result=calculator(num1,ope,num2)
print(result)

print("=======Calculator With if-elif-else: ==========")
#
#
# num1=int(input("Enter first number: "))
# ope=input("Enter operator: ")
# num2=int(input("Ener second number: "))
#
#
# if ope=='+':
#     print(num1+num2)
# elif ope=='-':
#     print(num1-num2)
# elif ope=="*":
#     print(num1*num2)
# elif ope=="/":
#     print(num1/num2)
# elif ope=="%":
#     print(num1/num2)
# elif ope=="//":
#     print(num1//num2)
# elif ope=="**":
#     print(num1**num2)
# else:
#     print("Enter somewith wrong.And so try again,please: ")









