#Function

#Calling a function
def my_function():
 print("hello world")
my_function()

#fahrenheit_to_celsius

def fahrenheit_to_celsius(fahrenheit):
 return(fahrenheit - 32) * 5 / 9
print(fahrenheit_to_celsius(59))
print(fahrenheit_to_celsius(90))

#Aruguments
def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")

#note: Parameter is the variable listed inside the () 
#      Aruguments are the actual value that is sent to the function

def my_function(name): # name is a parameter
  print("Hello", name)

my_function("Emil") # "Emil" is an argument

#number of Aruguments
def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes")

#default Parameter
def my_function(name = "friend"):
  print("Hello", name)

my_function("Emil")
my_function("Tobias")
my_function()
my_function("Linus")

#Keyword Arguments
def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function(animal = "dog", name = "Buddy")

#Positional Arguments
def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function("dog", "Buddy")

#Returning Different Data Types
def my_function():
  return ["apple", "banana", "cherry"]

fruits = my_function()
print(fruits[0])
print(fruits[1])
print(fruits[2])

#Positional-Only Arguments
def my_function(name, /):
  print("Hello", name)

my_function("Emil")

#Keyword-Only Arguments
def my_function(*, name):
  print("Hello", name)

my_function(name = "Emil")

#Local scope
def myfunc():
  x = 300
  print(x)

myfunc()

#global Scope
#A variable created in the main body of the code is a global variable and belongs to the global scope.
x = 300

def myfunc():
  print(x)

myfunc()

print(x)

#Global Keyword
#If you need to create a global variable, but are stuck in the local scope, you can use the global keyword
def myfunc():
  global x
  x = 300

myfunc()

print(x)

#NonLocal Keyword
#The nonlocal keyword is used to work with variables inside nested functions.

