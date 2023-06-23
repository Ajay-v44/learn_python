def reverse(name_rev):
    temp=name_rev
    temp2=""
    length=len(name_rev)
    for i in range(1,length+1):
        temp2+=name_rev[length -i]
    print("Reverse of word ::",temp2)
    if temp == temp2:
        print(temp,"is palindrome ")
    else:
        print (temp2 ,"is not palindrome ")

name=input ("Enter the word ::")
reverse(name)
