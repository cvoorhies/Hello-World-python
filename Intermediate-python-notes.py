print()
print()
print()
# Lists are created with square brackets
myList = ["banna", "cherry", "apple", "orange"]
print(myList)

myList2 = list() #use list function to create and empty list
print(myList2)

# To create a second list that is in a different order use the step method
myList2 = myList[::-1]
print(myList2)
# Becareful of copying lists. If you copy list to list any mods with change original list. 
# To copy use either .cop(), list(list_orig), or listcpy = list_Orig[:]

myList3 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
newList = [i*i for i in myList3]
print(myList3)
print(newList)

#Tuples are a list created with () and once made cannot be changed.
myTuples = ("clyde", 53, "Tracy")
print(myTuples)
# for tuples with only one item a comma must follow the item to make it a tuple
myTuples2 = ("clyde",)
print(type(myTuples2))

myTuples3 = tuple(["clyde", 53, "Tracy"])# created using function tuple to use on a list
print(myTuples3)

#unpacking tuples:
my_tuple1 = "Clyde", 53, "Tracy"
name, age, city = my_tuple1

print(name)
print(age)
print(city)
print(type(my_tuple1))
print()

import sys
my_list2 = [0, 1, 2, "Hello", True]
my_tuple4 = (0, 1, 2, "Hello", True)
print(sys.getsizeof(my_list2))
print(sys.getsizeof(my_tuple4)) # Tuples use less space than lists
print()

import timeit # calculates how long it takes to create a list vs tuple
print(timeit.timeit(stmt="[0, 1, 2, 3, 4, 5]", number=1000000))
print(timeit.timeit(stmt="(0, 1, 2, 3, 4, 5)", number=1000000))
print()

#Dictionaries: Key-value pairs, Unordered, Mutable, created with {}
mydict = {"name": "Clyde", "age": 53, "city": "Tracy"}
print(mydict)

#to add another elememt (Key & Value)
mydict["email"] = "MyOfficeSpace888@gmail.com"
print(mydict)

# To create a second list that is in a different order use the step method
myList2 = myList[::-1]
print(myList2)
# Becareful of copying lists. If you copy list to list any mods with change original list. 
# To copy use either .cop(), list(list_orig), or listcpy = list_Orig[:]

myList3 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
newList = [i*i for i in myList3]
print(myList3)
print(newList)

#Tuples are a list created with () and once made cannot be changed.
myTuples = ("clyde", 53, "Tracy")
print(myTuples)
# for tuples with only one item a comma must follow the item to make it a tuple
myTuples2 = ("clyde",)
print(type(myTuples2))

myTuples3 = tuple(["clyde", 53, "Tracy"])# created using function tuple to use on a list
print(myTuples3)

#unpacking tuples:
my_tuple1 = "Clyde", 53, "Tracy"
name, age, city = my_tuple1

print(name)
print(age)
print(city)
print(type(my_tuple1))
print()

import sys
my_list2 = [0, 1, 2, "Hello", True]
my_tuple4 = (0, 1, 2, "Hello", True)
print(sys.getsizeof(my_list2))
print(sys.getsizeof(my_tuple4)) # Tuples use less space than lists
print()

import timeit # calculates how long it takes to create a list vs tuple
print(timeit.timeit(stmt="[0, 1, 2, 3, 4, 5]", number=1000000))
print(timeit.timeit(stmt="(0, 1, 2, 3, 4, 5)", number=1000000))
print()

# Dictionaries: Collection data type, Key-Value pairs, Unordered, Mutable and created with {}
myDict = {"name": "Clyde", "age": 53, "city":"Tracy"}
print(myDict)

#to access the values:
value = myDict["name"]
print(value)
#to add another elememt (Key & Value)
myDict["email"] = "MyOfficeSpace888@gmail.com"
print(myDict)

# to delete items from a dict,  use keyword del, or pop("key") or
myDict.popitem()# takes the last item off of the dict
print(myDict)

#to find out if there is a key in a dict use this
if "age" in myDict:
    print("age")

#or
try:
    print(myDict["lastname"])
except:
    print("This will be the error message printed out")
print()

# To loop through the dict and get the key value pair use:

for key, value in myDict.items():
    print(key, value)

#When copying a dict avoid just asigning it to copy. If you make changes to one it changes the original
# use this methods for copying

myDict_Cpy = myDict.copy()
print(myDict_Cpy)
# or
myDict_Cpy = dict(myDict)
myDict["email"] = "MyOfficeSpace888@gmail.com"
print(myDict)
print(myDict_Cpy)

print()
done = input("are you done looking at results, hit enter")
