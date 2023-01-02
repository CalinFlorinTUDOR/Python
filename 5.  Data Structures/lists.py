arr = [1,2,3,4,5,6,7,8,9,10]
print(arr[0])
print(arr[5])
print(arr[9])

#Definition and accessing the values from the list
listX = ['AI&ML', 'TensorFlow', 1991, 2022]
listZ = [1, 2, 3, 4, 5, 6, 7]
print("listX[0]: ", listX[0])
print("listZ[1:5]: ", listZ[1:5])
print("listX[-1]: ", listX[-1])


#Concatenate
listA = [1, 2, 3]
listB = [4, 5, 6]
print(listA + listB)

#Length
print("The length of tuples is:",len(listA))

#Repetitions
listR = ["ROU"] * 3
print(listR)

#Iterations
for x_list in [1, 2, 3]:
    print(x_list)
    
#Apartenance
print(3 in [1, 2, 3])
print(9 in listB)

#Use of list-specific functions
print("Old:",listX)
listX.append("Data Science")
print("New:",listX)
listX.insert(2, "Test value")
print("New 2.0:",listX)
ret = listX.pop(3)
print("New 3.0:",listX)
print("The value returned and removed from the list is", ret)

newList = listA + listB
print("Generated list ", newList)
newList.reverse()
print("Reversed list ",newList)
newList.sort()
print("Sorted list ", newList)
newList.remove(2)
print("New list: ", newList)



b = [1,4,9,16,25,36,49,64,81,100]
for num in b:
    if num % 2 == 0:
        print(num)
        

list=[]
for i in range(10):
  print("Name ",i+1,": ",sep="",end="")
  name=input()
  list.append(name)

print("\n2.1.a ",sorted(list))

entries={}
for name in list:
  entries[name]=list.count(name)
print("\n2.1.b ",entries)

for key, value in entries.items():
  if list(entries.values())[0] == value:
    print("\n2.1.c ", list(entries.values())[0], " x ", key, sep="", end="")

  print()
for key, value in entries.items():
  if list(entries.values())[-1] == value:
    print("\n2.1.d ", list(entries.values())[-1], " x ", key, sep="", end="")

print("\n\n2.1.e ",sorted(list,reverse=True))

listA = []
listB = []
listN = []
listS = []
for i in range(0,len(list),2):
  listA.append(list[i])
  listB.append(list[i+1])
tuplA = tuple(listA)
tuplB = tuple(listB)
listA.append("")
listB.append("")
for i in range(5):
  listN.append(len(tuplA[i])+len(tuplB[i]))
listN.append(0)
for j in range(5):
  for i in range(5):
    if listN[i] < listN[i+1]:
      listA[i], listA[i+1] = listA[i+1], listA[i]
      listB[i], listB[i+1] = listB[i+1], listB[i]
      listN[i], listN[i+1] = listN[i+1], listN[i]
for i in range(len(listA)-1):
  listS.append(listA[i])
  listS.append(listB[i])

print("\n2.2 ",listS)


for i in range(0, 3464,2):
  if i % 7 ==0:
    print(i)
  if i==1332:
    break