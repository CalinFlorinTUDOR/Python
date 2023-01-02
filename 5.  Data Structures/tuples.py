#Definition and accessing the values of a tuple
food_tuple = ("Paste", "Banane", "Lava Cake", "Smoothie")
print(food_tuple)
print("I want to eat", food_tuple[2])

print("\n#Looping through the elements of a tuple using a for\n")
for food in food_tuple:
  print("Today, I have appetite to eat:", food)

#Secventions
tupX = ('Python', 'Jupiter', 1999, 2025)
tupZ = (1, 2, 3, 4, 5, 6, 7 )
print("tupX[0]: ", tupX[0])
print("tupZ[1:5]: ", tupZ[1:5])
#Concatenate
tupA = (1, 2, 3)
tupB = (4, 5, 6)
print(tupA + tupB)
#Length
print("The length of a tuple is:",len(tupA))
#Repetitions
tupR = ("ROU") * 4
print(tupR)
#Iterations
for x_tuple in (1, 2, 3):
  print(x_tuple)
#Appartenance
print(3 in (1, 2, 3))
print(9 in tupB)
#Erase
del tupR



tuplex = ("a", 5, "b", "c", "d", "e", "f", "g", "h", "i")
print("b" in tuplex)
print(9 in tuplex)


price = [('element1', '2.20'), ('element2', '20.5'), ('element3', '10.10')]
print( sorted(price, key=lambda x: float(x[1]), reverse=True))


def multiplication_of_elements(nums):
    temp = list(nums)
    multiplication = 1 
    for x in temp:
        multiplication *= x
    return multiplication

a = (4, 3, 2, 2, -1, 18)
print ("Tuple: ")
print(a)
print("Result of multiplication:",multiplication_of_elements(a))

a = (2, 4, 8, 8, 3, 2, 9)
print ("\nTuple: ")
print(a)
print("Result of tuple:",multiplication_of_elements(a))