n=int(input("Enter how many elements:"))
list=[]
evenlist=[]
oddlist=[]
for i in range(n):
    value=int(input("Enter any value:"))
    list.append(value)
print(list)
for value in list:
    if value%2==0:
        evenlist.append(value)
    else:
        oddlist.append(value)
print(evenlist)
print(oddlist)
