#Module 1
#This is a comment
print ("MODULE 1")
print ("Hello, python")

num = 2
name = "Jorim"
print (num)
print (name)
var = 5
var = "Loli"
print (var)
print()

print (type(num))
print (type(name))
print()

fruit1, fruit2, fruit3 = "Apple", "Watermelon", "Avocado"
print (fruit1)
print (fruit2)
print (fruit3)
print()

fruit1 = fruit2 = fruit3 = "Apple"
print (fruit1)
print (fruit2)
print (fruit3)
print()

a = "Python is incredible"
print (a)
print()

a = "Python"
b = "is"
c = "incredible"
print (a, b, c)
print()

num1 = 9
num2 = 6
print (num1 + num2)
print()

c = "incredible"
def myfunction1():
 print("Python is " + c)
myfunction1()
print()

c = "incredible"
def myfunction2():
 c = "amazing"
 print("Python is " + c)
print()

myfunction2()
print("Python is " + c)
print()

def myfunction3():
 global c
 c = "amazing"

 myfunction3()
 print("Python is " + c)
 print()

num1 = str ("33")
num2 = 22
print(num1, num2)
print()

#MODULE 2
print ("\n--------------------------------")
print ("MODULE 2")

num = 8
num1 = 565643331789939812
num2 = -98622366

print (type(num))
print (type(num1))
print (type(num2))
print()

num = 9.10
num1 = 6.0
num2 = -98.65

print (type(num))
print (type(num1))
print (type(num2))
print()

num = 74e6
num1 = 96E3
num2 = -66.7e980

print (type(num))
print (type(num1))
print (type(num2))
print()

print("Python")
print('Python')
print()

mString = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print()

print (mString)

aString = "Hi, Python!"
print(a[1])

lString = "Hi, Python!"
print (len(lString))

cString = "The best life ever!"
print("ever" in cString)

if "ever" in cString:
 print("Yes, 'ever' is present.") 
print()

sString = "Hi, Python!"
print(sString[3:6])
print(sString[:6])
print(sString[-6:-3])
print()

print(sString.upper())
print(sString.lower())
print()

wsString = "  Hello, World!"
print(wsString.strip())

print(sString.replace("H", "J"))

print(sString.split(","))
print()

a = "Hi"
b = "Python"
c = a + b
print(c)
print()

a = "Hi"
b = "Python"
c = a + " " + b
print (c)
print()

age = 20
txt =  "My name is Jorim, I am {}"
print(txt.format(age))
print()

numbers = 6
itemId = 99663
amount = 43.98
myrequest = "I want {} pieces of item no.{} for {} pesos."
print(myrequest.format(numbers, itemId, amount))
print()

myrequest = "I want to pay {2} dollars for {0} pieces of item no.{1}."
print(myrequest.format(numbers, itemId, amount))
print()

print (9 > 5)
print (6 == 9)
print (12 < 5)
print()

num1 = 600
num2 = 123

if num1 > num2:
 print("num1 is greater than num2")
else:
 print("num1 is not greater than num2")
print()

print(bool("Hi"))
print(bool(13))
print()

def myFunc() :
 return True

print(myFunc())
print()

print(9 + 3)
print()

#MODULE 3
print ("\n--------------------------------")
print ("MODULE 3")

num1 = 44
num2 = 400
if num2 > num1:
 print("num2 is greater than num1")
print()

num1 = 44
num2 = 44
if num2 > num1:
 print("num2 is greater than num1")
elif num1 == num2:
 print("num1 and num2 are equal")
print()

num1 = 400
num2 = 44
if num2 > num1:
 print("num2 is greater than num1")
elif num1 == num2:
 print("num1 and num2 are equal")
else:
 print("num1 is greater than num2")
print()

num1 = 400
num2 = 44
if num2 > num1:
 print("num2 is greater than num1")
else:
 print("num1 is greater than num2")
print()

if num1 > num2: print("num1 is greater than num2")
print()

num1 = 6
num2 = 235
print("A") if num1 > num2 else print("B")
print()

num1 = 400
num2 = 400
print("A") if num1 > num2 else print("=") if num1 == num2 else print("B")
print()

a = 100
b = 44
c = 400
if a > b and c > a:
 print("Both conditions are True")
print()

if a > b or a > c:
 print("At least one of the conditions is True")
print()

num1 = 44
num2 = 100
if not num1 > num2:
 print("a is NOT greater than  b")
print()

num = 21
if num > 5:
 print("Above ten,")
if num > 15:
 print("and also above 20!")
else:
 print("but not above 20.")
print()

if num2 > num2:
 pass

i = 2
while i < 5: 
 print(i)
 i += 1
print()

i = 2
while i < 5: 
 print(i)
 if i == 4:
  break
 i += 1
print()

i = 2
while i < 5: 
 i += 1
 if i == 4:
  continue
 print(i)
print()

i = 2
while i < 5: 
 print(i)
 i += 1
else:
 print("i is no longer less than five")
print()

animals = ["dog", "cat", "salagubang"]
for x in animals:
 print (x)
print()

for x in "cat":
 print(x)
print()

for x in animals:
 print (x)
 if  x == "cat":
  break
print()

for x in animals:
 if x == "cat":
  break
 print(x)
print()

for x in animals:
 if x == "cat":
  continue
 print(x)
print()

for x in range(5):
 print(x)
print()

for x in range (3, 7):
 print (x)
print()

for  x in range (6, 50, 9):
 print (x)
print()

for x in range (4):
 print(x)
else:
 print("Finished!")
print()

for x in range (4):
 if x == 2: break
 print(x)
else:
 print("Finished!")
print()

adj = ["adorable", "gentle", "cute"]
for x in adj:
 for y in animals:
  print (x, y)
print()

for x in [0, 1, 2]:
 pass

#MODULE 4
print ("\n--------------------------------")
print ("MODULE 4")

thisList = ["Computer" , "Laptop", "Smartphone"]
print(thisList)
print()

thisList = ["Computer" , "Laptop", "Smartphone", "Computer" , "Laptop"]
print(thisList)
print()

thisList = ["Computer" , "Laptop", "Smartphone"]
print(len(thisList))
print()

myList = ["Computer" , "Laptop", "Smartphone"]
print(type(myList))
print()

thisList = list(("Computer" , "Laptop", "Smartphone"))
print(thisList)
print()

thisList = ["Computer" , "Laptop", "Smartphone"]
print(thisList[1])
print(thisList[-1])
print()

thisList = ["Computer" , "Laptop", "Smartphone", "Charger", "Wifi"]
print(thisList[1:3])
print()

thisList = ["Computer" , "Laptop", "Smartphone", "Charger", "Wifi"]
print(thisList[-2:-1])
print()

thisList = ["Computer" , "Laptop", "Smartphone"]
if "Computer" in thisList:
 print("Yes, 'Computer' is in the list")
print()

thisList[1] = "Burger"
print(thisList)
print()

thisList = ["Computer" , "Laptop", "Smartphone", "Charger", "Wifi"]
thisList[2:3] = ["Burger", "Fries"]
print(thisList)
print()

thisList = ["Computer" , "Laptop", "Smartphone"]
thisList[1:2] = ["Burger", "Fries"]
print(thisList)
print()

thisList = ["Computer" , "Laptop", "Smartphone"]
thisList.insert(1, "Fries")
print(thisList)
print()

thisList.append("Keyboard")
print(thisList)
print()

thisList.insert(0, "Earphone")
print(thisList)
print()

thisList = ["Computer" , "Laptop", "Smartphone"]
parts = ["Earphone", "Keyboard"]
thisList.extend(parts)
print(thisList)
print()

thisList = ["Computer" , "Laptop", "Smartphone"]
food = ("Burger", "Fries")
thisList.extend(food)
print(thisList)
print()

thisList.remove("Laptop")
print(thisList)
print()

thisList.pop(3)
print(thisList)
print()

thisList = ["Computer" , "Laptop", "Smartphone"]
del thisList[1]
print(thisList)
print()

thisList.clear
print(thisList)

thisList = ["Computer" , "Laptop", "Smartphone"]
for x in thisList:
 print(x)
print()

for i in range(len(thisList)):
 print(thisList[i])
print()

i = 0
while i < len(thisList):
 print(thisList[i])
 i = i + 1
print()

[print(x) for x in thisList]
print()

gadgets = ["Computer" , "Laptop", "Smartphone", "Charger", "Wifi"]
newList = []

for x in gadgets:
 if "a" in x:
  newList.append(x)
print(newList)
print()

gadgets = ["Computer" , "Laptop", "Smartphone", "Charger", "Wifi"]
gadgets.sort()
print(gadgets)
print()

gadgets.sort(reverse= True)
print(gadgets)
print()

def myfunc(n):
 return abs(n - 50)
print()

numList = [200, 145, 72, 88, 50]
numList.sort(key = myfunc)
print(numList)
print()

caseList = ["yellow", "Violet", "Red", "blue"]
caseList.sort()
print(caseList)
print()

caseList.sort(key = str.lower)
print(caseList)
print()

caseList = ["yellow", "Violet", "Red", "blue"]
caseList.reverse()
print(caseList)
print()

myList = caseList.copy()
print(myList)
print()

myList = list(gadgets)
print(myList)
print()

list1 = ["x", "y", "z"]
list2 = [9, 8, 7]
list3 = list1 + list2
print(list3)
print()

list1 = ["x", "y", "z"]
list2 = [9, 8, 7]
for x in list2:
 list1.append(x)
 print(list1)
print()

list1 = ["x", "y", "z"]
list2 = [9, 8, 7]
list1.extend(list2)
print(list1)
print()

stuple = ("head", "shoulder", "knees")
print(stuple)
print(stuple[1])
print()

print(stuple[-1])
print()

bodyparts = ("head", "shoulder", "knees", "ear", "mouth", "nose", "eye")
print(bodyparts[3:5])
print(bodyparts[:2])
print(bodyparts[4:])
print(bodyparts[-3:-1])
if "knees" in bodyparts:
 print("Yes, 'knees is in the bodyparts tuple")
print()

bodyparts = ("head", "shoulder", "knees", "ear", "mouth", "nose", "eye")
x = list(bodyparts)
x[3] = "toes"
bodyparts = tuple (x)
print(bodyparts)
print()

x.append("finger")
bodyparts = tuple(x)
print(bodyparts)
print()

add = ("lips",)
bodyparts += add
print(bodyparts)
print()

x.remove("knees")
bodyparts = tuple (x)
print(bodyparts)
print()

animals = ("cat", "dog", "rat")
(tiger, lion, bat) = animals
print(tiger)
print(lion)
print(bat)
print()

animals= ("cat", "dog", "rat", "elephant", "frog")
(tiger, lion, *bat) = animals
print(tiger)
print(lion)
print(bat)
print()

animals= ("cat", "dog", "rat", "elephant", "frog")
(tiger, *sheep, bat) = animals
print(tiger)
print(sheep)
print(bat)
print()

animals = ("cat", "dog", "rat")
for x in animals:
 print(x)
print()

for i in range (len(animals)):
 print(animals[i])
print()

i = 0
while i < len(animals):
 print(animals[i])
 i = i + 1
print()

tuple1 = ("a", "b", "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)
print()

mtuples = animals * 3
print(mtuples)
print()

mySet = {"black", "gray", "white"}
print(mySet)
print(len(mySet))
print(type(mySet))
print()

mySet = set(("black", "gray", "white"))
print(mySet)
print()

for x in mySet:
 print(x)
print()

print("banana" in mySet)
print()

mySet.add("green")
print(mySet)
print()

mySet = {"black", "gray", "white"}
clothes = {"sleeves", "shirt", "jacket"}
mySet.update(clothes)
print(mySet)
print()

mySet = {"black", "gray", "white"}
clothes = ["sleeves", "shirt"]
mySet.update(clothes)
print(mySet)
print()

mySet.remove("black")
print(mySet)
print()

mySet.discard("gray")
print(mySet)
print()

x = mySet.pop()
print(x)
print(mySet)
print()

mySet = {"black", "gray", "white"}
mySet.clear()
print(mySet)
print()

mySet = {"black", "gray", "white"}
for x in mySet:
 print(x)
print()

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)
print()

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set1.update(set2)
print(set1)
print()

a = {"blue", "gray", "black"}
b = {"jacket", "gray", "shirt"}
a.intersection_update(b)
print(a)
print()

a = {"blue", "gray", "black"}
b = {"jacket", "gray", "shirt"}
c = a.intersection(b)
print(c)
print()

a = {"blue", "gray", "black"}
b = {"jacket", "gray", "shirt"}
a.symmetric_difference_update(b)
print(a)
print()

a = {"blue", "gray", "black"}
b = {"jacket", "gray", "shirt"}
c = a.symmetric_difference(b)
print(c)
print()

#MODULE 5
print ("\n--------------------------------")
print ("MODULE 5")

motorInfo = {
 "brand": "Honda",
 "model": "Click",
 "year": 2022
}
print(motorInfo)
print(motorInfo["brand"])
print()

motorInfo = {
 "brand": "Honda",
 "model": "Click",
 "year": 2022,
 "year": 2023
}
print(motorInfo)
print(len(motorInfo))
print()

motorInfo = {
 "brand": "Honda",
 "electric": False,
 "year": 2022,
 "color": ["white", "black", "gray"]
}
print(motorInfo)
print(type(motorInfo))
print()

motorInfo = dict(brand = "Honda",
                 model = "Click",
                 year = 2023)
print(motorInfo)
print()

motorInfo = {
 "brand": "Honda",
 "model": "Click",
 "year": 2022
}
x = motorInfo["model"]
y = motorInfo.get("model")
z = motorInfo.keys()
print(motorInfo)
motorInfo["color"] = "gray"
print(motorInfo)
a = motorInfo.values()
print(motorInfo)
motorInfo["year"] = 2024
print(motorInfo)
print()

b = motorInfo.items()
print(b)
motorInfo["year"] = 2021
print(b)

motorInfo = {
 "brand": "Honda",
 "model": "Click",
 "year": 2022
}

a = motorInfo.items()
print(a)
motorInfo["color"] = "white"
print(a)
print()

if "model" in motorInfo:
 print("Yes, 'model' is in motorInfo")
print()

motorInfo.update({"year": 2024})
print(motorInfo)
print()

motorInfo.pop("year")
print(motorInfo)
print()

motorInfo.popitem()
print(motorInfo)
print()

del motorInfo["model"]
print(motorInfo)

motorInfo.clear()
print(motorInfo)

motorInfo = {
 "brand": "Honda",
 "model": "Click",
 "year": 2022
}
for x in motorInfo:
 print(x)
 print(motorInfo[x])
print()

for x in motorInfo.values():
 print(x)
print()

for x in motorInfo.keys():
 print(x)
print()

for x, y in motorInfo.items():
 print(x, y)
print()

mydict = motorInfo.copy()
print(mydict)
print()

nbaplayer = {
 "player1" : {
  "name" : "Luka",
  "jnumber" : 77
 },
 "player2" : {
  "name" : "Kyrie",
  "jnumber" : 11
 },
 "player3" : {
  "name" : "KD",
  "jnumber" : 35
 }
}
print(nbaplayer)
print()

player1 = {
 "name" : "Luka",
 "jnumber" : 77
}
player2 = {
 "name" : "Kyrie",
 "jnumber" : 11
 }
player3 = {
 "name" : "KD",
 "jnumber" : 35
 }

nbaplayer = {
 "player1" : player1,
 "player2" : player2,
 "player3" : player3
}
print(nbaplayer)
print(nbaplayer["player3"]["name"])
print()

def my_function():
 print("Hello function")
my_function()
print()

def my_name(fname):
 print(fname + " Pablico")
my_name("jorim")
my_name("remjo")
my_name("remboi")
print()

def my_fullname(fname, lname):
 print(fname + " " + lname)

my_fullname("Jorim", "Pablico")
print()

def my_kids(*kids):
 print("The youngest child is " + kids[2])
my_kids("James", "Johnny", "Totoy")
print()

def child(child3, child2, child1):
 print("The youngest child is " + child3)
child(child1="James", child2="Johnny", child3="Totoy")
print()

def lname_kid(**kid):
 print("His last name is " + kid["lname"])
lname_kid(fname = "Jorim", lname = "Pablico")
print()

def my_places(country = "Philippines"):
 print("I am from " + country)
my_places("Korea")
my_places("Japan")
my_places()
my_places("China")
print()

def my_func(food):
 for x in food:
  print(x)
print()

fruits = ["orange", "avocado", "mango"]
my_func(fruits)
print()

def my_func(x):
 return 6 * x
print(my_func(4))
print(my_func(2))
print(my_func(7))
print()

def tri_recursion(k):
 if k > 0:
  result = k + tri_recursion(k - 1)
  print(result)
 else:
  result = 0 
 return result
print("\n\nRecursion Example Results")
tri_recursion(6)
print()

def hello(name):
 print("Hello, " + name)

import mymodule
mymodule.hello("Jorim")

import mymodule
a = mymodule.person1["age"]
print(a)

import mymodule as mx
a = mx.person1["age"]
print(a)

import platform
x = platform.system()
print(x)
print()

import platform
x = dir(platform)
print(x)
print()

def greeting(name):
 print("Hello, " + name)

person1 = {
 "name": "Jorim",
 "age": 20,
 "country": "Philippines"
}

from mymodule import person1
print(person1["age"])
print()

import datetime
x = datetime.datetime.now()
print(x)
print(x.year)
print(x.strftime("%A"))

x = datetime.datetime(2020, 5, 4)
print(x.strftime("%B"))

#MODULE 6
print ("\n--------------------------------")
print ("MODULE 6")

import mysql.connector

mydb = mysql.connector.connect(
 host="localhost",
 user="root",
 password="Awit83:18",
 database="mydatabase"
)
mycursor = mydb.cursor()

mycursor.execute("SHOW DATABASES")
for x in mycursor:
 print(x)
print()

mycursor.execute("DROP TABLE customers")
mycursor.execute("DROP TABLE users")
mycursor.execute("DROP TABLE products")

mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")
mycursor.execute("SHOW TABLES")
for x in mycursor:
 print(x)
print()

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)" 
val = ("Juan", "Pasay") 
mycursor.execute(sql, val)
mydb.commit()
print(mycursor.rowcount, "record inserted.")
print()

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = [
  ('Pedro', 'Caloocan'),
  ('Ricardo', 'Valenzuela'),
  ('Mang Ben', 'Manila'),
  ('Wally', 'Cavite'),
  ('Diwata', 'Bagiuo'),
  ('Violetta', 'Taguig')
]

mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "was inserted.")
print()

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("Mitch", "Caloocan")
mycursor.execute(sql, val)
mydb.commit()
print("1 record inserted, ID:", mycursor.lastrowid)
print()

mycursor.execute("SELECT * FROM customers")
myresult = mycursor.fetchall()
for x in myresult:
  print(x)
print()

mycursor.execute("SELECT name, address FROM customers")
myresult = mycursor.fetchall()
for x in myresult:
  print(x)
print()

#mycursor.execute("SELECT * FROM customers")
#myresult = mycursor.fetchone()
#print(myresult)
#print()

sql = "SELECT * FROM customers WHERE address='Valenzuela'"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
  print(x)
print()

sql = "SELECT * FROM customers WHERE address LIKE '%way%'"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
  print(x)
print()

sql = "SELECT * FROM customers ORDER BY name"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
  print(x)
print()

sql = "SELECT * FROM customers ORDER BY name DESC"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
  print(x)
print()

sql = "DELETE FROM customers WHERE address = 'Manila'"
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount, "record(s) deleted")
print()

sql = "DROP TABLE customers"
mycursor.execute(sql)

sql = "DROP TABLE IF EXISTS customers"
mycursor.execute(sql)

mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = [
  ('Pedro', 'Caloocan'),
  ('Ricardo', 'Valenzuela'),
  ('Mang Ben', 'Manila'),
  ('Wally', 'Cavite'),
  ('Diwata', 'Bagiuo'),
  ('Violetta', 'Taguig')
]

mycursor.executemany(sql, val)

mydb.commit()

sql = "UPDATE customers SET address = 'Baguio' WHERE address = 'Cebu'"
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount, "record(s) affected")
print()


mycursor.execute("SELECT * FROM customers LIMIT 5")
myresult = mycursor.fetchall()
for x in myresult:
  print(x)
print()


mycursor.execute("SELECT * FROM customers LIMIT 5 OFFSET 2")
myresult = mycursor.fetchall()
for x in myresult:
  print(x)
print()


mycursor.execute("CREATE TABLE users (id INT, name VARCHAR(255), fav VARCHAR(255))")
sql = "INSERT INTO users (id, name, fav) VALUES (%s, %s, %s)"
val = [
  (1, 'Pedro', '123'),
  (2, 'Ricardo', '125'),
  (3, 'Mang Ben', '125'),
  (4, 'Wally', ''),
  (5, 'Diwata', '')
]
mycursor.executemany(sql, val)
mydb.commit()

mycursor.execute("CREATE TABLE products (id INT, name VARCHAR(255))")
sql = "INSERT INTO products (id, name) VALUES (%s, %s)"
val = [
  (123, 'Crushed Oreos'),
  (125, 'Mango Graham'),
  (126, 'Halo-Halo')
]
mycursor.executemany(sql, val)
mydb.commit()

sql = "SELECT \
  users.name AS user, \
  products.name AS favorite \
  FROM users \
  INNER JOIN products ON users.fav = products.id"

mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
  print(x)
print()

sql = "SELECT \
  users.name AS user, \
  products.name AS favorite \
  FROM users \
  LEFT JOIN products ON users.fav = products.id"

mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
  print(x)
print()

sql = "SELECT \
  users.name AS user, \
  products.name AS favorite \
  FROM users \
  RIGHT JOIN products ON users.fav = products.id"

mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
  print(x)