#Problem - 03 [Marks - 25]

# testcase = int(input())

#sets = int(input())
num = int(input())
start = 0
end = num

while start < end:
    NN = int(input())
    if NN % 2 == 0:
        print("yes")
    else:
        print("no")
    start += 1

"""start = 0
end = int(input())
while start < end:
    sets = int(input())
    result = sets*15
    print (result)
    start += 1"""