def first_function():
  print('Hi!')
  print('This is my first function')
  print('I feel good, I am progressing :)')
first_function()

def function_arg(name, age):
  print('My name is ', name,' and I have', age,' years old')
function_arg('Michael', 35)

def functionArg(name, age):
  print('My name is ', name,' and I have', age,' years old')
name = 'Michaela'
age = 25
functionArg(name, age)

def maximumValue( x, y ):
    if x > y:
      print(x)
    else:
      print(y)
maximumValue(4, 17)

def maximumValue( x, y ):
    if x > y:
      return x
    else:
      return y
res = maximumValue(43, 27)
print('The final result is', res)


def getName():
  name = input('Enter your name:')
  return name
def getUser():
  user = input('Enter your username:')
  return user
def getPassword():
password = input('Enter your password:')
while len(password) < 5:
    print('Your password is too short. Try once again')
parola = input('Enter your password:')

name = getName()
user = getUser()
password = getPassword()

def secPassword(password):
    passwordSec = hash(parola)
    return passwordSec

def getDataUser(name, user, password):
    print('User identification data are', name, user, password)
    
passSec = secPassword(password)
print('Password', password, "has been secured and is", passSec)
getDataUser(name, user, passSec)

def valueMax( x, y ):
    if x > y:
      return x
    else:
      return y
def numberMax( x, y, z ):
      return valueMax( x, valueMax( y, z ) )
print(numberMax(2, 7, -2))

def fact(n):
    if n == 1:
      return 1
    else:
      return (n * fact(n - 1))
print(fact(5))


def main():
    print('main code')
    
def func():
    print('func')
    
func()
if __name__ == "__main__":
    main()
    
def multiply():
    print(2*3)
    
def func():
    print('func1')
def main():
    multiply()
    func()
main()


def max_of_two( x, y ):
    if x > y:
        return x
    return y
def max_of_three( x, y, z ):
    return max_of_two( x, max_of_two( y, z ) )
print(max_of_three(7, 10, -3))

def string_reverse(str1):

    rstr1 = ''
    index = len(str1)
    while index > 0:
        rstr1 += str1[ index - 1 ]
        index = index - 1
    return rstr1
print(string_reverse('adfxcva'))

def prime_number(n):
    if (n==1):
        return False
    elif (n==2):
        return True
    else:
        for x in range(2,n):
            if(n % x==0):
                return False
        return True             
print(prime_number(31))
