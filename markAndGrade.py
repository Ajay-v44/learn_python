list=[]
for i in range(5):
 num1=int(input("enter you mark out of 100 of subject  \t"))
 list.append(num1)
sum=sum(list)
average=sum/5
print("your average is ",average)
percentage=(sum/500)*100
if percentage>=90:
 print("A+")
elif percentage>=80:
 print("A")
elif percentage>=70:
 print("B+")
elif percentage>=60:
 print("B")
elif percentage>=50:
 print("c+")
else:
 print("you are falied")