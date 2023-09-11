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

#Sets: Unordered, mutable, no duplicates ( previous data structures can have duplicates)
#Sets are created with Curly brackets like a dict but no key/value pairs. Just items seperated with a colon.
mySet = {1, 2, 3, 4, 5, 6, 7, 8, 9}
print(mySet)
mySet2 = set("Hello World")
print(mySet2)
#To create a empy set you have to use the set() method.
#use .add method to add to a set
mySet.add(10)
mySet2.add("A")
print(mySet)
print(mySet2)
# To remove elements use the .remove() or the .discard() and to empty set us .clear. .pop() woks as well
#unions, and intersections
setOdd = {1,3,5,7,9}
setEven = {2, 4, 6, 8, 10}
setPrime = {2, 3, 5, 7}

myUnion = setOdd.union(setEven)
print(myUnion)

myIntersection = setOdd.intersection(setPrime)
print(myIntersection)

diff = setOdd.difference(setEven) # Prints everything not in setEven
diff2 = setOdd.symmetric_difference(setEven) #Prints everything that is in setOdd and SetEven that are not in both sets
print(diff)
print(diff2)

#Use setA.union or difference or symetric_difference_update(setB) to change a set

# Supersets and disjoints methods
setA = {1, 2, 3, 4, 5, 6}
setB = {1, 2, 3}

print(setA.issubset(setB)) # result is false because neither set has the same items
print(setA.issuperset(setB)) # result is True because its the opposite of subset. 

#.isdisjoint() gives True only if both sets don't have any of the same items.

#frozen set is also a data collection type which is a immutable version of a set

#strings: ordered, immutable, text representation. using triple quotes is for multiline strings

my_String = 'How,are,you,doing' 
my_List = my_String.split(",") # uses the , as a delimiter and splits each word as 1 element in the list
print(my_List)





print()
done = input("are you done looking at results, hit enter")
