# -*- coding: utf-8 -*-
"""updated_BiweeklyChallenge3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1xT1OmsE-_nzOs66RRXG9-PMA5kx2BjP-

Bi Weekly Challenge - 
which is to collect user input, 
confirm user category for his/her current age group,
and also shows users age in the next 5 decade.
'''
"""

le

#Collecting USERS INPUT.
try:
  name = input('Type in your name: ')
  age = int(input('How old are you: '))
  gender = input('What is your gender: ')
  year = 2021
except ValueError:
  print('Oops that was not a valid number')
except TypeError:
  print('Argument must be a number')
if gender == 'M' or gender == 'Male':
  print('Hello Mr {} You are {}'.format(name, age))
elif gender == 'F' or gender == 'Female':
  print('Hello Mrs {} You are {}'.format(name, age))
else:
  print('Hello {} You are {}'.format(name, age))

#YEAR OF BIRTH
print('Your year of birth is {}'.format(year-age))

#CONFIRMING USERS CATEGORY. 
if (age > 65): 
  cat = 'Older Adults'
elif (age > 18) & (age < 65):
  cat = 'Adult'
elif (age > 12) & (age < 18):
  cat = 'Teens'
elif (age > 1) & (age < 11):
  cat = 'Childer'
else:
  cat = 'Infants'
print('As you are {} years old, you are an {}'.format(age, cat))

#SHOWING USERS AGE IN 5 DECADE.
new_age = []
new_year = []
for i in range(10,61, 10):
  new_a = age + i
  new_age.append(new_a)
  new_y = year + i
  new_year.append(new_y)

for i in range(len(new_age)):
  a = new_age[i]
  b = new_year[i]
  print('In {}, you would be {} year of age'.format(b,a))