#1. Access List Item

#items are indexed and you can access them by referring to the index number
thislist = ["apple", "banana", "cherry"]
print(thislist[1])

#Negative indexing means start from the end
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

#Range of Indexes
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])
print(thislist[:4])
print(thislist[2:])

#Check if
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")

#2. Change list Item
#Using Range
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

#using insert method
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

#3. Addd list Item
#using append() method
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

#Using insert() method
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)

#Using extend() method
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

#4. Remove list Item
#Sepcified Item using remove() method
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

#Sepcified Index using pop() method
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
thislist.pop() #If the index is not specified, it will remove the last item
print(thislist)

#Using clear() method empties the list
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

#5. Loop Lists
#Use the range() and len() method in for loop
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])

#While loop
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

#6. List Comprehenion
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

#newlist = [expression for item in iterable if condition == True]

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)

#7. Sort Lists
#using sort() method it will always sort in acending order
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

#sort() method for descending
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)

#8. Copy Lists
#using copy() method
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

#using list() method
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

#9. Join Lists
#using a + operator which used to join or concatenate 2 or more lists
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

