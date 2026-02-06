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
def myfunc1():
  x = "Jane"
  def myfunc2():
    nonlocal x
    x = "hello"
  myfunc2()
  return x

print(myfunc1())

#Lambda Functions
#syntax: lambda arguments : expression
x = lambda a, b, c : a + b + c
print(x(5, 6, 2))

#using function
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))

#Using Lambda with map()
numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)

#Using Lambda with filter()
#function creates a list of items for which a function returns True
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
print(odd_numbers)

#Using Lambda with sorted()
#function can use a lambda as a key for custom sorting
students = [("Emil", 25), ("Tobias", 22), ("Linus", 28)]
sorted_students = sorted(students, key=lambda x: x[1])
print(sorted_students)

#Recursion
#Recursion is when a function calls itself. the benefit of meaning that you can loop through data to reach a result.
def countdown(n):
  if n <= 0:
    print("Done!")
  else:
    print(n)
    countdown(n - 1)

countdown(5)

#Base Case and Recursive Case
def factorial(n):
  # Base case - A condition that stops the recursion
  if n == 0 or n == 1:
    return 1
  # Recursive case - The function calling itself with a modified argument
  else:
    return n * factorial(n - 1)

print(factorial(5))

#Fibonacci Sequence
def fibonacci(n):
  if n <= 1:
    return n
  else:
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(7))

#Recursion with Lists
def sum_list(numbers):
  if len(numbers) == 0:
    return 0
  else:
    return numbers[0] + sum_list(numbers[1:])

my_list = [1, 2, 3, 4, 5]
print(sum_list(my_list))

