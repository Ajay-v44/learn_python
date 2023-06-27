rows = int(input('Enter the number of rows: '))


i = 1
while i <= rows:
    
    j = rows - i
    while j > 0:
        print(" ", end='')
        j -= 1
    
    
    k = 1
    while k <= i:
        print("*", end=' ')
        k += 1
    
    print()
    i += 1
