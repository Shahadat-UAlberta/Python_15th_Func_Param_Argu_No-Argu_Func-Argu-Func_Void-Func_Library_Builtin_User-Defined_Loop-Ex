"""

* Mir Ahamadul Hoque [4178259]

* Rahul Borma [4174857]

* Ajay Ghosh [4178225] (2)

* Tanvir Rahman (4170467)

* Azad Hossan (4170669)

*  MD. Amirul Islam (4176218)

* Shamim Hossen



"""

list = []                                                           # List Declaration
lstNumber = int(input("How many number you want in the list:"))     # List value/number input
sumList = []
#sum = 0

start = 0                                       # Starting point of iteration
while start < lstNumber:                        # While Loop condition
    number = int(input("Enter The numbers: "))  # To take input
    list.append(number)
    start = start + 1
print("Inputted list is:", list)

start = 0

while start < lstNumber:
    sumNumber = list[start]            #int(input(list[index]))

    if start == 0:
        sumList.append(sumNumber)
        
    else:
        sumList.append(sumList[start-1] + sumNumber)

    start = start + 1

print("Sum list is:", sumList)

"""
lst = [1,2,3,4]
outputLst = []
start = 0
end = len(lst)

while start < end:

    innerStart = 0
    innerEnd = start
    innerSum = 0

    while innerStart < innerEnd:
        innerSum += lst[innerStart]
        innerStart += 1

    innerSum += lst[start]
    outputLst.append(innerSum)
    start += 1


print(outputLst)

"""
