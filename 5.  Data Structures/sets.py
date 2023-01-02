vacation_set = {"Bora Bora", "Las Vegas", "Tenerife"}
print (vacation_set)

vacation_set = {"Bora Bora", "Las Vegas", "Tenerife", "Las Vegas"} # duplicate value same result as above
print(vacation_set)

print("\n#Adding elements into a set\n")
vacation_set.add("San Torini")
vacation_set.add("Las Vegas") 
print(vacation_set)
print("\n#Erease elements from set\n")
vacation_set.remove("Bora Bora")
print(vacation_set)
print("\n#Update a set with a list (or between two sets)\n")
vacation_list = ["Bali", "Monaco", "Fiji", "Australia", "Bali"]
print(vacation_list)
vacation_set.update(vacation_list)
print(vacation_set)
print("\n#Union of two sets\n")
rou_vacations = {"Brasov", "Maramures", "Constanta", "Hateg"}
wish_list_vacations = vacation_set.union(rou_vacations)
print(wish_list_vacations)
print("\n#Looping elements from set using a for\n")
current_year = 2021
for loc in wish_list_vacations:
  print("I plan to travel in " + loc + " in year " + str(current_year))
current_year = current_year + 1
print("\n#Erase the values from a set\n")
wish_list_vacations.clear()
print(wish_list_vacations)


set_C = {"Verde", "Galben", "Albastru", "Alb"}
print("Elements:")
print(set_C)        
print("\n After erase the elements:")
set_C.clear()
print(set_C)


x = {2,3,4}
y = {4,5,6,7}
z = {9}
print("Elements:")
print(x)
print(y)
print(z)
print("\n Verify if they have elements in common:")
print("\nCompare x and y:")
print(x.isdisjoint(y))
print("\nCompare x and z:")
print(z.isdisjoint(x))
print("\nCompare y and z:")
print(y.isdisjoint(z))


a = {1,2,3,4,5}
b = {4,5,6,7,8}
print("Sets:")
print(a)
print(b)
print("Difference between a and b using difference:")
print(a.difference(b))
print("Difference between b and a using difference:")
print(b.difference(a))
print("Difference between a and b using -")
print(a-b)
print("Difference between b and a using - :")
print(b-a)