from functionLibrary.FunctLIB import hello


print("Hello World!!!")
x = 10
x = (x+25)/5
print(x)
x='Clyde'
print(x)
print(0 == 0.0)
print(0 is 0.0)
print(0 != 0.0)

#This is how to setup constants in python
from enum import Enum
class State(Enum):
    CONSTANT1 = 12
    #CONSTANT2 = input("set the constant to ")

print(State.CONSTANT1.value)
#print(State.CONSTANT2.value)

# Tuples are constant lists that can't be modified.
# Dictionaries are Key:Value pairs

employee1 = { "fname" : "Clyde", "lname": "Voorhies", "empNum": 7, "pay": "$55"}
employee2 = { "fname" : "Sam", "lname": "Beau", "empNum": 10, "pay": "$35"}
print(employee2["fname"])

dicEmps = (employee1, employee2)
print(dicEmps[1]["pay"])
print(dicEmps[0].get("pay"))
print(list(employee1.keys()))
print(list(employee1.values()))
employee1["status"] = "Perm"
employee2["status"] = "Temp"

print(list(employee1.keys()))
print(list(employee2.values()))

#sets - are like Tuples but can be modified and looks like a dict without the keys
set1 = {"Clyde", "Sam", "Terry"}
set2 = {"Clyde", "Sam"}
intersect = set1 & set2
print(intersect)
mod = set1 | set2 # use "-" to get difference of sets, <> to see if items are in both sets.
print(mod)


# Classes
class Animal:
    def walk(self):
        print("Walking...") # showing inheartance of classes

class Dog(Animal):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self): # self always has to be included in methods and intanciation
        print("Woof, Woof!")

rodger = Dog("Rodger", 8)
rodger.bark()
rodger.walk()

hello() #imported from function library

# Lambda functions
result = lambda num : num * 2

multiply = lambda a, b : a * b

print(multiply(2,4))
print(result(5))

# map, filter, reduce used on lists to manipulate the list to a new list

# Recursion

def factorial(n):
    """ this is a docstring used to annotate what programs are doing and utilize
    the help to get more information about it.This function will give you the factorial of a number
    """
    if n==1 : return 1
    return n * factorial(n-1)
    

print(factorial(5))



print(help(factorial))

print("End of notes")
hit_enter = input("hit enter to end program")