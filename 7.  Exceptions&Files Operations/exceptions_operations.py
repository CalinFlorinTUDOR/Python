# how is generated exceptions in Python

k = None
if k == None:
  raise Exception('The value of variable is undefined')

o = 3
d = "Str"
g = o + d
print(g)

# solve the error

o = 3
d = "Str"
g = str(o) + d
print(g)

# how to treat exceptions 

l = [1, 2, 3, 4]
for r in range(6): # better modify the range in 4
  print(l[r])
  
# solve the error

l = [1, 2, 3, 4]
try:
    for r in range(6):
      print(l[r])
except IndexError:
    print('list size exceeded')
    
# divide by 0

x = 21
y = 0
z = x / y
print(z)
print('The program was ended successfully')

#solve error

try:
  x = 21
  y = 0
  z = x / y
except ZeroDivisionError:
    print('Operation Not allowed')
print('The program was ended successfully')


f = open("test.txt", "r")
f.read()
print('The program was ended successfully')

# solve the error

try:
  f = open("test.txt", "r")
  f.read()
except FileNotFoundError:
  print('There is no test.txt')
print('The program was ended successfully')


m = [9, 8, 7, 6, 5]

def listPrint(ls):
  for x in range(len(ls)):
    print (ls[x])
listPrint(m)


e = "Big string"
print(e[20])

# solve error

try:
  e = "Big string"
  print(e[20])
except IndexError:
  print('size exceeded')
print('The program was ended successfully')

