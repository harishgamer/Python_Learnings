#Identity and Membership Operators
#is / == Returns True if both variables are the same object
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)
print(x is y)
print(x == y)

#is / != not Returns True if both variables are not the same object
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is not z)# returns False because z is the same object as x

print(x is not y)# returns True because x is not the same object as y, even if they have the same content

print(x != y)# to demonstrate the difference betweeen "is not" and "!=": this comparison returns False because x is equal to y

#in Returns True if a sequence with the specified value is present in the object
fruits = ["apple", "banana", "cherry"]

print("banana" in fruits)
 
#not in Returns True if a sequence with the specified value is not present in the object
fruits = ["apple", "banana", "cherry"]

print("pineapple" not in fruits)