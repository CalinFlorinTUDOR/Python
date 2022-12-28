# numbers variables

x = 5   #integers
y = -10
a = 5.1 # float
b = 6.3
print(x)
print(y)
print(a)
print(b)

sum = x + y #assignment operators
print(sum)
print('Sum is:', sum)

x = 7
y = 15
sum = x + y
print(sum)
sum += 3
print('Sum is:', sum)

x = 7
y = 15
sum = x + y
print(sum)
sum -= 3  # combined operators
print('Sum is:', sum)

x = 7
y = 15
sum = x + y
print(sum)
sum *= 3
print('Sum is:', sum)

x = 7
y = 15
sum = x + y
print(sum)
sum /= 3
print('Sum is:', sum)

x = 7
y = 15
sum = x + y
print(sum)
sum %= 3
print('Sum is:', sum)

# string variables

four_letters = 'Abcd'
print(four_letters)

four_letters = four_letters + 'a'
print(four_letters)
print(len(four_letters))

print('Our string has', four_letters, ' and has the length of', len(four_letters))

charA = 'This morning I drank'
charB = 'coffee'
charC = 'tea'
print('charA[0] is', charA[0])
print(charA[15])
print(charB[3:6])
print(charC[1:3])
print(charB[-3:-1]) # fe

charA = 'This morning I drank'
charB = 'coffee'
sentence = charA + charB
print(sentence)

# correct way

charA = 'This morning I drank'
charB = 'coffee'
sentence = charA + ' ' + charB # This morning I drank coffee
print(sentence)

print('Yesterday' + ' d' + charA[1:] + ' ' + charB) # Yesterday dhis morning I drank coffee

# concatenate 

a=49

print('My age is' + a)
print('My age is'+str(a))

print('My age','is 49', sep='\n')

print('First sentence', end='.')
print('Second sentence', end='.')
print('Third sentence', end='.')

print('A','B','C', sep=',', end='.')

firstname = 'Michael'
lastname = 'Johnson'
lastname = 'Stan'
age = 40
age += 1
salary = 3900.99
salary %= 1000
print(firstname)
print(lastname)
print(age)
print(salary)

question = input ('Hi! How are you?')
print('User answer is:', question)



k = int(20)
l = int(-5)
m = float(8.73)
n = str('Python')
o = str('I love programming in ')
p = str('because the sum of those two numbers is: ')

print(k)
print(l)
print(m)
print(n)
print(o)
print(p)

sentence_two = o + ' ' + n + ' ' + p 
print(sentence_two)
print('All variables has been initialized')

x = -7 + 4/3*5
y = -7 + 4/(3*5)
z = (-7 + 4/3)*5

print("x=",x)
print("y=",y)
print("z=",z)