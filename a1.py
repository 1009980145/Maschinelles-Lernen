#A1
a=["a",2]
b=[2,3]
c=(a,b)
print("list_combination",c)
a1=len(a)
b1=len(b)
list1=[]
for i in range(a1):
    for j in range(b1):
        tup=(a[i],b[j])
        list1.append(tup)

print(list1)
