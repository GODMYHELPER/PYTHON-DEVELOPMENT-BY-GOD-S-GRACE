def greet():
    print("My name is Divine.")

greet()
greet()

def greet(name):
    print("Hello", name)

greet("John")
greet("Mary")

def show():
    print("I am learning Python!")

show()
show()

def add(a, b):
    return a + b
result = add(5, 3)
print(result)

def add(a, b):
    return a + b
print(add(3,5))

age = int(input("What is your age?" ))
if age <= 13:
    print("Child")
elif age <= 17:
    print("Teen")
else:
    print("Adult")