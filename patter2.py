rows =int(input("Enter the rows"))
i=1
inc=1
while i<=rows+2:
    j=1
    while j<=i:
        print(inc,end='  ')
        inc+=1
        j+=1
    print()
    i+=2

