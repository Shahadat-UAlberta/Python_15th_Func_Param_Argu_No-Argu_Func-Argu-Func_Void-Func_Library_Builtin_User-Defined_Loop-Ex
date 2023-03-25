number = int(input("Take an intput: "))
start = 1
end = number
while start <= number:
    if number % start == 0:
        print(start)
    start += 1


