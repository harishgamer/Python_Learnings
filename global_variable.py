#varaible outsid the function is global variable
variable = "fun"

def func():
  print("Python is " + variable)

func()

#we can also use global keyword to delcare
def func1():
  global a
  a = "fun"

func1()

print("Python is " + a)
