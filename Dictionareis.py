#Dictionareis
# It used to store data value in key:value pairs
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

#it is changeable which means we can add (or) remove items after the dictionary has been created.
#Dictionaries won't Allow Duplicates but code will run also len() keyword is used to check no.of.item in the dictionary and items can be #only data type(str, int, float, Boolean, list, etc..) 

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(type(thisdict))

#Access Items
#you can access the itemsof a dictionary by referring to its key name inside [] and also with get() method

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]
print(x)
x = thisdict.get("model")
print(x)

#using 3 method we will be accessing the Items - keys() , values(), items()

#keys()
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()
print(x) #before the change

car["color"] = "white"
print(x) #after the change

#values()
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values()
print(x) #before the change

car["year"] = 2020
print(x) #after the change

#items()
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.items()
print(x) #before the change

car["year"] = 2020
print(x) #after the change

#Change Dictionarey Items
#we can change the value of specific items by referring to is key name and also using update() method
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

#Update and Add Dictionary item
#note : Update and Add are pretty similar because if you ue update() method for a same key: value it wil be update but if you use 
#different key:value it will be add to th edictionary items.

thisdict["year"] = 2018

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020})

#adding
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"color": "red"})

#Remove Dictionary item
#Using pop(), popitem(), clear(), del()

#pop()
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)

#popitem()
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict)

#clear()
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict)

#del()
"""thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict
print(thisdict) #this will cause an error because "thisdict" no longer exists."""

#Loop Dictionareies
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict:
  print(thisdict[x])

"""
note: 
values() method

for x in thisdict.values():
  print(x)

keys() method

for x in thisdict.keys():
  print(x)

iems() method

for x, y in thisdict.items():
  print(x, y)
"""
 

#Copy a Dictionary
#you can't copy a dictionary simply by dict2 = dict 1 because dict2 will only reference to dict1. Using copy() method
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)

#using dict() method
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = dict(thisdict)
print(mydict)

#Nested Dictionaries
#If dictionary contains dictionaries is called nested dictionary, it can be in 2 ways.
#1st wy
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

print(myfamily)

#2nd way
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}

print(myfamily)


