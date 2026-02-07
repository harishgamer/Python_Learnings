#Tuple
#It is used to store multiple items in a single variable. the tuple is ordered and unchangeable, it is mentioned as () where duplicate value are allowed
#It can be any data type
thistuple = ("apple", "banana", "cherry")
print(thistuple)

#Allow duplicates
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)

print(tuple1)
print(tuple2)
print(tuple3)

#tuple() constructor
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)

#Accesss tuple by referring to the Index numbers
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

#negatvie index -1 refer to the last item, -2 refers to the second last item
thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])#range Index

#Check the tuple using in
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")

#change the tupple value
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

#using append() method
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)

thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)

#using remove() method
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)

#unpacking tuple
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

#using Asterisk* If the number of variables is less than the number of values, you can add an * to the variable name and the values will be assigned to the variable as a list
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)

#loop Tuple which is done with for and while loop 
thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])

thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1

#Join tuple are done with to operator's which are + and * operator
#2 tuple joint
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)

#multiply tuple
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)




