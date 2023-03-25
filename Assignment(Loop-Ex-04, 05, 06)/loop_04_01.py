#Problem - 01 [Marks - 25]
number = int(input("Take an intput: "))
start = 1
end = number
while start <= end:
    # start += 1
    if number % start == 0:
        print(start)
    start += 1