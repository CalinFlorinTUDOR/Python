my_dictionary = {
"key_1": "value_1",
"key_2": "value_2"
}
print(my_dictionary)

print("#Create dictionary - represents name and bank account in EUR of the persons\n")
my_dictionary = {
"Michael": 4832,
"Jason": 683
}
print(my_dictionary)
print("\n#1 - Add elements in dictionary\n")
my_dictionary["Adam"] = 2149
print("Dictionarul actualizat 1.0:\n", my_dictionary)
my_dictionary["Anne"] = 3434
my_dictionary["Alexander"] = 1204
my_dictionary["Dan"] = 1378
my_dictionary["John"] = 932
print("Upgraded dictionary 2.0:\n", my_dictionary)
print("\n#2 - Getting the value based on a given key\n")
value_exA = my_dictionary["Adam"]
print("The value from Adam account is:", value_exA)
#using get() method
value_exB = my_dictionary.get("Adam")
#same result
print("The value from Adam account is:", value_exB)
print("\n#3 - Modify elements (existing elements)\n")
print("#The initial value from Adam's account is: " + str(my_dictionary["Adam"]) + " EUR")
my_dictionary["Adam"] = 7777 #initial value was 2149
print("#The value from Adam's account is: " + str(my_dictionary["Adam"]) + "EUR")
print("##The initial value from John's account is:  "  + str(my_dictionary["John"]) + " EUR")
initial_sum = my_dictionary["John"]
new_sum = initial_sum * 2
my_dictionary["John"] = new_sum
print("##The updated value from John's account is:  "  +str(my_dictionary["John"]) + " EUR")

print("\n#4 - Looping the dictionary using for\n")
key = my_dictionary.items()
for key in my_dictionary:
  print("The amount of money available in this account " + key + " is "+ str(my_dictionary[key]) + " EUR")
print("\nWe give a bonus to everyone...\n")
#We give 150 EUR to everyone
for key in my_dictionary:
  my_dictionary[key] = my_dictionary[key] + 150
print("The NEW amount of money available in this account " + key + " is "+ str(my_dictionary[key]) + " EUR")

print("\n#5 - Erase the elements\n")
no_elements = len(my_dictionary)
print("The dictionary contains " + str(no_elements) + " elements")
my_dictionary.pop("Adam")
print("The dictionary without Adam:\n", my_dictionary)
no_elements = len(my_dictionary)
print("The dictionary contains " + str(no_elements) + " elements")
#using del
del my_dictionary["John"]
print("The dictionarul without Adam and John:\n", my_dictionary)
no_elements = len(my_dictionary)
print("The dictionary contains " + str(no_elements) + " elements")
#clear all elements from dictionary, keeping the variable my_dictionary in memory
my_dictionary.clear()
no_elements = len(my_dictionary)
print("This dictionary contains " + str(no_elements) + " elements")
#erase all dictionary including variable my_dictionary from memory
del my_dictionary

nested_dict = {
"d1": { 'key_1': 'value_1', 'key_2': 'value_2'},
"d2": { 'key_3': 'value_3', 'key_4': 'value_4'}
}
print(nested_dict)
print(nested_dict["d1"])
print(nested_dict["d2"])

nested_dict = {
"d1": { 'key_1': 'value_1', 'key_2': 'value_2'},
"d2": { 'key_3': 'value_3', 'key_4': 'value_4'}
}
print(nested_dict)
print(nested_dict["d1"])
print(nested_dict["d2"])
print("\nCreate nested dictionary\n")
personal_data = {
"p1": { 'name': 'Adam', 'income': 1000, 'age': 28},
"p2": { 'name': 'Emanuel', 'income': 2750, 'age': 36},
"p3": { 'name': 'George', 'income': 1750, 'age': 31}
}
print(personal_data)
print(personal_data["p1"])
print(personal_data["p2"])
print(personal_data["p3"])
print("\n#Adding an element\n")
personal_data["p4"] = { 'name': 'Daniel', 'income': 0, 'age': 16, 'job':
'Internship'}
print(personal_data)
print("\n#Erase an element\n")
del personal_data["p2"]
print(personal_data)


phone_dictionary = {
"Michael": +40757444444,
"Jason": +40757555555,
"Andrew": +40757777777,
"Christian": +40757222222,
"George": +40757111111,
"Wilma": +40757333333,
"Brenda": +40757666666,
"Zoe": +40757999999,
"Dexter": +40757666666,
"Xander": +40757888888
}
print(sorted(phone_dictionary))


price = [('Shoes', '45.50'), ('Jacket', '35'), ('Pullover', '41.30'), ('Shirt', '55'), ('T-shirt', '24')]
print( sorted(price, key=lambda x: float(x[1]), reverse=True))



my_dict ={"Andrew": 45, "Adam": 35, "Alice": 25}

key_list = list(my_dict.keys())
val_list = list(my_dict.values())
position = val_list.index(45)
print(key_list[position])

