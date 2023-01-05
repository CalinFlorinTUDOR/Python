#Classes in Python

class FirstClass:
  firstWord = "Hello!"
  firstNo = 51
  secondNo = -21
obj = FirstClass()

print(obj.firstWord)
print(obj.firstNo)
print(obj.secondNo)
print(obj.firstNo - obj.secondNo)

class MainClass:
    """This is a class with introductive purpose"""
varA_class = 12345
varB_class = 54321
def doSomething(self):
    print("I am here to show you the value of attributes:", self.varA_class,
self.varB_class )
    
def changeVar(self,var):
  var %= 10
  return var
obj = MainClass()
obj = doSomething()
print("The value of varA_class is:", obj.changeVar(obj.varA_class))
print("The value of varA_class is:", obj.changeVar(obj.varB_class))

class Person:
  def __init__(self, name, age, gender, nid):
    self.name = name
    self.age = age
    self.gender = gender
    self.nid = nid

persA = Person("Michael", 18, "Male", 1944686546)
print(persA.name)
print(persA.age)
print(persA.gender)
print(persA.nid)

class Person:
  def __init__(self, name = 'Nobody', age = 0, gender = 'N/A', nid = 0):
    self.name = name
    self.age = age
    self.gender = gender
    self.nid = nid

persB = Person()
print(persB.name)
print(persB.age)
print(persB.gender)
print(persB.nid)

class Person:
  def __init__(self, name = "Nimeni", age = 0, gender = "N/A", nip = 0):
    self.name = name
    self.age = age
    self.gender = gender
    self.nip = nip
def __str__(self):
  return 'Person(name=' + self.name + ', age=' + str(self.age) +', gender=' + self.gender + ', nip=' + str(self.nip) +')'

print(persA)
print(persB)

class Student:
    def __init__(self, name="Nimeni", age=0, gender="N/A", nid=0):
#var is public
      self.name = name
#var is protected, can be accessed from inside of class or class child from class Person
      self._age = age
#var is private (cant be accessed from outside of class)
      self.__gender = gender
#var is private (cant be accessed from outside of class)
      self.__nid = nid
      
stud = Student("Alex", 23, "M", 198)
print (stud.name)
print (stud.gender)
print (stud.age)

import random
class Student:
  ... #values definition from above
def studentRandom(self):
    randNr = random.randint(1, 10)
    return self.nume + str(randNr)
def __getRandom(self): # private method
    return self.studentRandom()
def randomFun(self, value):
    return "Random is: " + self.__getRandom() + " " + value
stud = Student("Alex", 23, "M", 198)
print (stud.name)
print (stud.studentRandom())
print (stud.randomFun("Tadaa"))
print (stud.__getRandom())

def getName(self):
  return self.name
print("My name is " + persA.getName())

def setName(self, value):
    self.name = value

persA.setName("Andrew")
print( "My name is " + persA.getName() )

class Person:
  def __init__(self, name="Nobody", age=0, gender="N/A", nip=0):
    self.name = name
    self.age = age
    self.gender = gender
    self.nip = nip
#definim metode de tip getter
def getName(self):
  return self.name
def getAge(self):
  return self.age
def getGender(self):
  return self.gender
def getNIP(self):
  return self.nip
#definim metode de tip setter
def setName(self, value):
  self.name = value
def setAge(self, value):
  self.age = value
def setGender(self, value):
  self.gender = value
def setNIP(self, value):
  self.nip = value
def __str__(self):
  return 'Person(name=' + self.name + ', age=' + str(self.age) +', gender=' + self.gender + ', nip=' + str(self.nip) + ')'
persA = Person()
print( "My name is " + persA.getName() )
persA.setName("Andrew")
print( "My name is " + persA.getName() )
persB = Person("Michael", 29, "Male", 1234)
print(persB)

persA.setAge("22")
print( "My age is " + persA.getAge() )
persA.setGender("Male")
print( "My gender is " + persA.getGender() )
persA.setNIP("1234567889")
print( "My NIP is " + persA.getNIP() )



class MyFamily():
    no_persons = 0
    def __init__(self):
        self.firstname = None
        self.lastname = None
        self.age = None
        self.motto = None
        self.hobbies = []
        print("Empty constructor")

    def __init__(self,firstname, lastname, age, motto, hobbies=[]  ):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.motto = motto
        self.hobbies = hobbies
        self.no_persons = self.no_persons + 1
    def getfirstname(self):
        return self.firstname
    def setfirstname(self, firstname):
        self.firstname = firstname

    def getlastname(self):
        return self.lastname
    def setlastname(self, lastname):
        self.lastname = lastname

    def setage(self, age):
        self.age = age
    def getage(self):
        return self.age

    def getmotto(self):
        return self.motto
    def setmotto(self,motto):
        self.motto = motto

    def gethobbies(self):
        return self.hobbies
    def setpasiuni(self, hobbies):
        self.hobbies = hobbies

p1 = MyFamily ("Andreas","Thomas",23,"Choose the long way because is straight  ",["tennis","football","curling"])
p2 = MyFamily ("Kimmich","Joshua",24,"Mens sana in corpore sano",["athletism","bob","cyclism"])
print (p1.getfirstname())
print (p2.getage())
p1.setlastname("Lewandowski")
print (p1.getlastname())
print(p1.gethobbies())
print(p1.getmotto())


# Inheritance
import random
class Person:
  def __init__(self, name="Nobody", age=0, gender="N/A", nip=0):
    self.name = name
    self.age = age
    self.gender = gender
    self.nip = nip
def __str__(self):
    return 'Person(name=' + self.name + ', age=' + str(self.age) + ', gender=' + self.gender + ', nip=' + str(self.nip) + ')'
def getName(self):
  return self.name
def getAge(self):
  return self.age
def getGender(self):
  return self.gender
def getNIP(self):
  return self.nip
def setName(self, value):
  self.name = value
def setAge(self, value):
  self.age = value
def setGender(self, value):
  self.gender = value
def setNIP(self, value):
  self.nip = value
class Student(Person): #class Student inheritance class Person
  def __init__(self, name="Nobody", age=0, gender="N/A", nip=0):super().__init__(name,age,gender,nip) #receive initialization of values from parent class
def studentRandom(self):
  randNr = random.randint(1, 10)
  return self.name + str(randNr)
def __getRandom(self):
    return self.studentRandom()
def randomFun(self, value):
    return "Random is: " + self.__getRandom() + " " + value
stud = Student("Alex", 23, "M", 198)
#usable examples from parent class from child class
print (stud.getName())
stud.setAge(29)
print (stud.getAge())
stud.setNIP(192)
print (stud.getNIP())
print (stud.studentRandom())
print (stud.randomFun("Tadaa"))

class Car():
  def __init__(self, brand, body, fuel, price, priceNegotiable):
    self.brand = brand
    self.body = body
    self.fuel = fuel
    self.price = price
    self.priceNegociable = priceNegotiable
def getBrand(self):
  return self.brand
def getBody(self):
  return self.body
def setBody(self, body):
  self.body = body
def getFuel(self):
  return self.fuel
def setFuel(self, fuel):
  self.fuel = fuel
def getPrice(self):
  return self.price
def setPret(self, price):
  self.price = price
def getPriceNegociable(self):
  return self.priceNegociable
def setPriceNegociable(self, priceNegociable):
  self.priceNegociable = priceNegociable
  
  
  
class BMW(Car):
  def __init__(self, body, fuel, model, color,
km , cPower,  speedMax, price, priceNegotiable):
    super().__init__("BMW", body, fuel, price, priceNegotiable)
    self.model = model
    self.color = color
    self.km = km
    self.cPower = cPower
    self.speedMax = speedMax
    print("The brand car " + super().getBrand() + " and model " + self.model + " it was created.")
def getModel(self):
  return self.model
def setModel(self, model):
  self.model = model
def getColor(self):
  return self.color
def setColor(self, color):
  self.color = color
def getcPower(self):
  return self.cPower
def setcPower(self, cPower):
  self.cPower = cPower
def getSpeedMax(self):
  return self.speedMax
def setSpeedMax(self, speedMax):
  self.speedMax = speedMax
def startEngine(self):
  print("Vmmmmm")
def stopEngine(self):
  print("Brrmmmm")
def revEngine(self):
  print("VMMMMMMMMMM")
def accelerate(self):
  print("PFIUUUHHH")
#we will create an instance of class BMW and initialize variables: body, fuel, model, color, km, cPower, speedMax, price and priceNegotiable
bA = BMW("SUV", "Diesel", "X6", "White", 120000, 300, 260, 45000,'N')
bA.startEngine()
bA.revEngine()
bA.accelerate()
bB = BMW("Sedan", "Diesel", "530d", "Black", 90000, 240, 230, 34000, 'Y')
bB.startEngine()
bB.revEngine()
bB.accelerate()
