#instead

i = 0
sum = 0
a = 5

if i == 0:
  sum = sum + a
  
i += 1
if i == 1:
  sum = sum + a + i
  
i += 1
if i == 2:
  sum += a + i
  
i += 1
if i == 3:
  sum += a + i
i += 1
print("Sum is: ", sum)

# we can do this

sum = 0
a = 5
ii = [0, 1, 2, 3]

for i in ii:
  sum += a + i
print("Sum is: ", sum)

#or

sum = 0
a = 5

for i in range(4): # for range(9) sum will be 81
  sum += a + i
print("Sum is: ", sum)

# with while

a = 5
sum = 0
while i <= 3:
  sum += a + i
i += 1
print("Sum is: ",sum)

a = 3
b = 9
x = 4  #x = 1, x = 8, x = 10, x = -1, x = 5.6
for i in range(a,b+1): 
  if x == i:
    print ('x is found in interval [a,b]')
  break

if i == b:
    print ('x is not found in interval')
    
# with while

a = 3
b = 9
x = 5
i = a
while i <= b:
  if x == i:
    print ('x is found in interval [a,b]')
    break
  
if i == b:
  print ('x is not found in interval')
i += 1
    
    
sum=0
for i in range(0,100):
  sum+=i
print("Sum of numbers from 0 to 100 is %d" % (sum))

k = 0
while k < 100:
  k += 1
print("Sum of numbers from 0 to 100 is %d" %(sum))


a=int(input("Enter initial number: "))
b=int(input("Enter the number up to which you want the addition to be made: "))
for i in range(a,b):
  a+=i
print("Sum of numbers from A to Z is %d" % (a))

c=int(input("\nEnter initial number: "))
d=int(input("Enter the number up to which you want the addition to be made: "))
while a<100:
  a+=1
print("Sum of numbers from A to Z is %d" %(a))


