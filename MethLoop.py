i = input("Tafel van?")
i2 = int(i)
num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
solve = int(0)
for i in num:
    solve = i2 * i
    print(str( i2) + ' × ' + str(i) + ' = ' + str(solve))