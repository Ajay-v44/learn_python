def operation(num3,num4,operator):
    if operator=="+":
        return num3+num4
    elif operator=="-":
        return num3-num4
    elif operator=="/":
        return num3/num4
    elif operator=="%":
        return num3%num4
    elif operator=="**":
        return num3**num4
    elif operator=="//":
        return num3//num4
    else :
        print("wrong input")

num1=int(input("enter a number"))
num2=int(input())
op=input("enter a operator")
print(operation(num1,num2,op))
