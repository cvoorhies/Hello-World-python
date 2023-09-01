

print("Hello World!!!")
x = 10
x = (x+25)/5
print(x)
x='Clyde'
print(x)
print(0 == 0.0)
print(0 is 0.0)
print(0 is not 0.0)

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