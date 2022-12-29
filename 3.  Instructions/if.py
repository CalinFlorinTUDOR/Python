a = 6
res = 0

if a > 3:
  res = a + 1
print(res)

a = 6
res = 0

if a > 9:
  res = a + 1
print(res)

b = 7
res_b = 0

if b > 10:
  res_b = b - 2
else:
  res_b = b + 2
print(res_b)

c = 2
res_c = 0

if c > 3:
  res_c = c - 1
elif c == 3:
  res_c = c
elif c < 3:
  res_c = c + 1
else:
  print("No results for res_c.")
print(res_c)

studentGrade = 10
subject = "Mathematics"

if studentGrade < 5:
  print("The student did not pass at the subject: ", subject)
elif studentGrade >= 5 and studentGrade < 10:
  print("The student passed the subject: ", subject)
elif studentGrade == 10:
  print("The student is awarded at the subject: ", subject)
else:
  print("The note entered is not correct")
  
  
d = int(input('Enter a number: '))

if d % 2 == 0:
  print('The number is even')
elif d % 2 != 0:
  print('The number is odd')
else:
  print('Error')

  
e = input("What is your name?")
f = input("What kind of job you like ?")
g = input("How long do you think you can get this job?")
h = input("What are the steps you have to follow to be able to get hired?")
i = input("When do you want to start?")

print("The candidate " + e + ", answered to the questions like this: "+ f +", "+ g +", "+ h +", "+i)


def isPalindrome(s):
  return s == s[::-1] #verifying if string S is equal with the reverse of the same string

j = input("Enter a word: ")  #Bob, Eve, Hannah, civic, level, minim, madam
revw = isPalindrome(j)

if revw:
  print("The word is a palindrome")
else:
  print("The word is not a palindrome")