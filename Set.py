#Set
#Sets are used to store multiple items in a single variable and also it is one of the 4 Data types
#It is a collection which is unordered, unchangeable*, and unindexed.
#It can be any data type

thisset = {"apple", "banana", "cherry"}
print(thisset)

set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}

print(set1)
print(set2)
print(set3)

#set() constructor to make a set.
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)

#set items using a for loop, or ask if a specified value is present in a set, by using the in keyword.
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

#using add() and updated() method
thisset = {"apple", "banana", "cherry"}

thisset.add("orange")
print(thisset)

thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)
print(thisset)

#using remove(), discard(), pop(), clear(), del() method
thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")
print(thisset)

thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")
print(thisset)

thisset = {"apple", "banana", "cherry"}

x = thisset.pop()

print(x)
print(thisset)

thisset = {"apple", "banana", "cherry"}

thisset.clear()
print(thisset)

thisset = {"apple", "banana", "cherry"}

del thisset
print(thisset)