list=[]
for i in range(3):
 num=input("enter  number")
 list.append(num)
 


if list[0]>list[1] and list[0]>list[2]:
    print(list[0],"is larger")
elif list[1]>list[0] and list[1]>list[2]:
    print(list[1],"is larger")
else:
    print(list[2],"is larger")