list1=["bmw","benz","audi","jaguar"]
print(list1)
print(list1[1])
if "bmw" in list1:
    print("yes present")
else:
    print("not")
#list1[1]="RR"
list1.insert(1,"rr")
print(list1)
for x in list1:
    print("elemnent "+x)