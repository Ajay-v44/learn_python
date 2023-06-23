name=input ("Enter the word ::")
temp=name
temp2=""
length=len(name)
for i in range(1,length+1):
    sub=name[length-i]
    temp2+=name[length -i]
print("Reverse of word ::",temp2)
if temp==temp2:
   
