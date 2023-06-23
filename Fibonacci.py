limit=int(input ("enter"))
num1=0
num2=1
print ("Fibonacci series are",num1,num2)
for i in range(1,limit+1):
    num3=num1+num2
    print( num3)
    num1=num2
    num2=num3
    
