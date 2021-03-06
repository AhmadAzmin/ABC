# -*- coding: utf-8 -*-
"""PythonBootcamp.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ohEfajcLdgi6vDcqQ8OZa5kvur6CFv2A

##1. ARITHMETIC OPERATION

###Simple Arithmetic
"""

a=5
b=6
c=a+b
print(c)

"""###Simple Arithmetic - Get input from User (+,-,*,%)"""

a = float(input("Enter the value of a: "))
b = float(input("Enter the value of b: "))
add=a+b
print(add)

a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
add=a+b
sub=a-b
mult=a*b
div=a/b
mod=a%b
print("ADD:",add)
print("Sum: {0}, Diff: {1}, Mult: {2}, Div:{3}, Mod:{4}".format(add,sub,mult,div,mod)) #Print using Format

print("Sum: %d, Diff: %d, Mult: %d, Div:%15.6f, Mod:%d"%(add,sub,mult,div,mod)) #Print using PADDING & PRECISION

print('{0:<4} | {1:^4} | {2:^4} | {3:>4}'.format('Sum','Diff','Mult','Div'))
print('{0:<4} | {1:^4} | {2:^4} | {3:>4}'.format(add,sub,mult,div))

"""###Simple Arithmetic - Get input from User (power)"""

a=2
b=3
power=a**b #Power
print(power)

"""##2. STRINGS

###Create String
"""

a = 'Python'
b = "Bootcamp"
print(a+b)

"""###Length of String"""

a="Champ"
print(len(a))

a="S"
b=a*5
print(b)

"""###String Index """

a="champ"
print(a[3]) #identifing the element based on index
print(a[2:]) #Grab the remaing elements except upto the Index
print(a[:2]) #Grab the elements upto the Index
print(a[-1]) #Grab the Last element
print(a[:-1]) #Grab the elements except last element
print(a[::2]) #Grab everything with 2 steps
print(a[::-1]) #Print string backwards

"""###String Functions"""

a="Master Class"
print(a.upper()) #Changing to Upper case
print(a.lower()) #Changing to Lowerb= a.split() case

b= a.split() #Splitting String
print(b)
print(b[1]) #Printing the splitting string based on Index

c="ElonMusk,SteveJobs,BillGates"
d=c.split(",") #Splitting string based on Delimitter
print(d)
print(d[1])

a="Master Class"
print(f"Welcome to Python {a} !") #Formatting string Literals

"""##3. LIST

###Create List
"""

a = [1,2,3,4,5]
b = ["Champ",21,99.5]
print(a,b)
print(len(b)) #Length of List
print(b[0]) #Locate list element based on Index
print(a[1:]) #print elements except 1st
print(a[:2]) #Print elements upto 2nd element
print(a+b) #Concatenate 2 list

a = [1,2,3,4,5]
a.append(6) #inserting new elements to the existing list
print(a)

a = [1,2,3,4,5]
a.reverse() #Reverse list
print(a)
print(min(a)) #Minimum
print(max(a)) #Maximum

a = [1,2,3,4,5]
from random import shuffle
shuffle(a)
a

a=[1,2,3]
b=[4,5,6]
c=[a,b] #Nested List Matrix
print(c)
print(c[0]) #Printing row
print(c[0][0]) #Printing 1st element

"""##4. DICTIONARIES

###Creating Dictionary : Key & Value
"""

a = {"Name":"Elon","Age":50,"Company":["SpaceX","Tesla"]}
a

a = {"Name":"Elon","Age":50,"Company":["SpaceX","Tesla"]}
print(a["Name"]) #Printing value based on its Key
a["Age"]= 51 #Changing values
a

b={"Climate":{"Condition":{"Temperature":"38 Degree","Humidity":"70 Percentage"}}}
print(b["Climate"]["Condition"]["Humidity"])

print(a.keys()) #Printing Keys of the Dictionaries
print(a.values()) #Printing Values of the Dictionaries
print(a.items()) #Printing Tuple of the all items

"""##5. TUPLES

###Creating Tuples
"""

a = ("Champ",21,99.5)
a

print(len(a)) #Length of tuple
print(a[0]) #Printing elements from tuple via index
print(a.index("Champ")) #Getting Index of Elements

"""##6. SETS

###Creating Set
"""

a = set()

a.add("Champ")
a

a.add(30)
a

b = ["Champ",21,99.5]
set(b)

"""##7. BOOLEAN

###Creating Boolean
"""

a = True

a = 10
b = 5
c=15
print(a<b)
print(a>b)
print(a==b)
print(a!=b)
print(a<=b)
print(a>=b)
print(a<b and c>a)
print(a<b or c>a)

"""##8.Python Statements

###If
"""

a = True
if a:
  print("Positive")
else:
  print("negative")

a=10
b=6
c=6

if a<b:
  print("a less than b")
elif c==b:
  print("a is equal to b")
  print("a is not less than b")
  if c<a:
    print("c is less than b")
else:
  print("a is not less than b")

"""###For"""

a = [1,2,3,4,5,6,7,8,9,10]
for i in a:
  print(i)

a = [i for i in 'Champ']
a

"""###Odd & Even Number"""

a = [1,2,3,4,5,6,7,8,9,10]
for i in a:
  if i % 2 == 0:
    print(i,"Even Number")
  else:
    print(i,"Odd Number")

"""###String - For"""

for a in "Hello all":
  print(a)

"""###Dictionary - For"""

a = {"Name":"Elon","Age":50,"Company":["SpaceX","Tesla"]}
for k,v in a.items():
  print(k)
  print(v)

"""###While"""

a=0
while a <11:
  print(a)
  a+=1 #a=a+1

"""### While - Break & Continue"""

a=0
while a < 10:
  print(a)
  a+=1
  if a==5:
    print("a is equal to 5")
    break
  else:
    print("Continueeee")
    continue

"""###Range"""

for a in range (6):
  print(a)

for a in range (1,10,1):
  print(a)

for a in range (10,0,-3):
  print(a)

a = [i**2 for i in range(0,5)]
a

a = [i for i in range(10) if i % 2 == 0]
a

"""### Enumerate - To track no. of iteration in the loop, without working with variable increament """

a=0
for i,a in enumerate("Hello Champ"):
  print(i,a)

"""### Zip - Creating a tuples by zipping 2 list"""

a = ["Name","Age","Country"]
b = ["Champ",27,"India"]
list(zip(a,b))