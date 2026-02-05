#module
def greeting(name):
  print("Hello, " + name)

#Nameing a Module
#you can name the module file whatever you like, but it must have the file extension .py
import mymodule as mx

a = mx.person1["age"]
print(a)

#import from Module
#you can choose to import only parts from a module, by using the from keyword.
#The module named mymodule has one function and one dictionary
def greeting(name):
  print("Hello, " + name)

person1 = {
  "name": "John",
  "age": 36,
  "country": "Norway"
}

#Import only the person1 dictionary from the module:
from mymodule import person1

print (person1["age"])