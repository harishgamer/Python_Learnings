#find() Method finds the first occurrence of the specified value. string.find(value, start, end)
txt = "Hello, welcome to my world."

x = txt.find("welcome")

print(x)

#islower() Method returns True if all the characters are in lower case, otherwise False.
txt1 = "hello world!"

x = txt1.islower()

print(x)

#casefold() Method returns a string where all the characters are lower case.
txt = "Hello, And Welcome To My World!"

x = txt.casefold()

print(x)

#count() method returns the number of times a specified value appears in the string.
txt = "I love apples, apple are my favorite fruit"

x = txt.count("apple")

print(x)

#isalnum method eturns True if all the characters are alphanumeric, meaning alphabet letter (a-z) and numbers (0-9).
txt = "Company12"

x = txt.isalnum()

print(x)

#index() method finds the first occurrence of the specified value and raises an exception if the value is not found. string.index(value, start, end)
txt = "Hello, welcome to my world."

x = txt.index("welcome")

print(x)

#isalpha() method Returns True if all characters in the string are in the alphabet
txt = "CompanyX"

x = txt.isalpha()

print(x)

#isupper() method Returns True if all characters in the string are upper case
txt = "THIS IS NOW!"

x = txt.isupper()

print(x)

#replace() method Returns a string where a specified value is replaced with a specified value
txt = "I like bananas"

x = txt.replace("bananas", "apples")

print(x)

#strip() method Returns a trimmed version of the string
txt = "     banana     "

x = txt.strip()

print("of all fruits", x, "is my favorite")

#split() method Splits the string at the specified separator, and returns a list
txt = "welcome to the jungle"

x = txt.split()

print(x)

#title() method Converts the first character of each word to upper case
txt = "Welcome to my world"

x = txt.title()

print(x)

