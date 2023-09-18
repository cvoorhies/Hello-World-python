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
new_string = ' '.join(my_List) # adding a space or , or something it seperates each item by that thing. In this case a space
print(new_string)

#Formating strings using %, .format(), and f-strings
var = 'Clyde'
my_String = 'the variable is %s' % var # the s is for string, if the variable was a decimal use d or if float use f
print(my_String)


var = 3.145
my_String = 'the variable is {:.2f}'.format(var) # the :.2f is to limit the decimal point
print(my_String)


var = 3.145
var2 = 88
my_String = f'the variable is {var} and {var2}'
print(my_String)

#Collections - Counter, namedtuple, orderedDict, defaultdict, deque

from collections import Counter
a = "aaaaabbbbccccddddddd"
my_Counter = Counter(a)
print(my_Counter) ### this gives a dictionary with key value setup like Counter({'d': 7, 'a': 5, 'b': 4, 'c': 4})
print(my_Counter.most_common(2)) # gives the key/value of the greatest values

#namedtuples
from collections import namedtuple
Point = namedtuple('Point', 'x,y')
pt = Point(1, -4)
print(pt)
print(pt.x, pt.y)


#OrderedDict is used to remember the order items were inserted. This is from an older version \
# of python and isn't used much any more.

#defaultDict is the same as a dict except it has a default value if the key has not been set
from collections import defaultdict
d = defaultdict(float)
d['a'] = 1
d['b'] = 2
print(d['c']) #give a default value of 0.0

#deque ('deck')
from collections import deque
d = deque()

d.append(1)
d.append(2)

d.appendleft(3)
print(d)

d.popleft()
print(d)
d.append(3)
d.extendleft([4, 5, 6, 7])
print(d)
d.rotate(2) 
print("""'rotated 2 to the left'""")
print(d)

print("""'itertools: product, permutations, combinations, accumulate, groupby, and infinite iterators'""")
# gives a cartesian list of points, i.e. matrix calculations
from itertools import product
a = [1, 2]
b = [3, 4]
prod = product(a,b)
print(list(prod))

from itertools import permutations # good for finding various combonations to a cypher.
a = [1, 2, 3, 4]
perm = permutations(a, 2) # the 2 is length of permutations, and is optional
print(list(perm))

from itertools import combinations # just like a permutation except the length is required
a = [1, 2, 3, 4]
comb = combinations(a, 3)
print(list(comb))

from itertools import accumulate
a = [1, 2, 3, 4]
acc = accumulate(a)
print(a)
print(list(acc))

import operator # to multiply the outputs
a = [1, 2, 3, 4]
acc = accumulate(a, func=operator.mul)
print(a)
print(list(acc))

# groupby itertool
from itertools import groupby
def smaller_than_3(x):
    return x < 3
a = [1, 2, 3, 4]
group_obj = groupby(a, key=smaller_than_3) #can use a lambda function for the key, lambda x: x<3
for key, value in group_obj:
    print(key, list(value))

# another groupby example:
persons = [{'name': 'Tim', 'age':25}, {'name': 'Dan', 'age': 25}, 
           {'name': 'Lisa', 'age': 27}, {'name': 'Claire', 'age': 28}]

group_obj = groupby(persons, key=lambda x: x['age'])
for key, value in group_obj:
    print(key, list(value))

#Lambda function review: lambda arguments: expression
add10 = lambda x: x + 10 
print(add10(5)) # result is 15

points2D = [(1, 2), (15, 1), (5, -1), (10, 4)]
points2D_sorted = sorted(points2D, key=lambda x: x[1])

print(points2D)
print(points2D_sorted) # sorted by y index

#map(func, seq(or a list))
a=[1, 2, 3, 4, 5, 6]
b = map(lambda x: x*2, a)
print(list(b))

c= filter(lambda x: x%2==0, a)
print(list(c))

from functools import reduce
product_a = reduce(lambda x, y: x*y, a)
print(product_a)

#****************** Exceptions ************************
# Syntax ore Exception errors
# Exceptions are runtime errors
# Use the 'Raise Exception('Error message you want to show up') to 
# create your own errors
# Example
#x = -5
#if x < 0:
#    raise Exception('X should be positive')
# Assert errors
#x =-5
#assert (x>=0), 'x is not positive'
#
# try/except error handling
#try:
#   a = -5/0
#except:
#   print('An error has occurred')
#try:
#   a = -5/0
#except Exception as e:
#   print(e) // gives a "divide by zero error message"
#   a = 5/1
#   b = a / '10
#except ZeroDivisioinError as e:
#   print(e) // gives a "divide by zero error message"
#except TypeError as e:
#   Print(e)  // gives a type error message
#else:
#   print('Everything is fine') /// prints this message if no error is found
#finally:
#   print('Cleaning up...') used to clean up or fix errors found. Error message will still be printed
#### To create your own error message use:
# class ValueTooHighError(Exception):
#   pass
# class ValueTooSmallError(Exception):
#   def _init_(self, message, value):S
#       self.message = message
#       self.value = value
#def test_value(x):
#   if x > 100:
#       raise ValueTooHighError('Value is too high')
#   if x < 5:
#       raise ValueTooSmallError('Value is too small', x)
#test_value(200) // gives the error message
# or you can do it this way
#try:
#   test_value(200) // gives the error message
#except ValueTooHighError as e:
#   print(e) give just the error message
#except ValueTooSmallError as e:
#   print(e.message, e.value)

# Logging 
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    datefmt='%m/%d/%y %H:%M:%S')
logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message') # with just these 5 messages only the warning and higher will be printed if the basicConfig message isn't there
logging.error('This is an error message')
logging.critical('This is a critical message')

import Helper
######### handler logging
logger = logging.getLogger(__name__)

# Create handler
stream_h = logging.StreamHandler()
file_h = logging.FileHandler('file.log')

# level and the format
stream_h.setLevel(logging.WARNING)
file_h.setLevel(logging.ERROR)

formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
stream_h.setFormatter(formatter)
file_h.setFormatter(formatter)

logger.addHandler(stream_h)
logger.addHandler(file_h)

logger.warning('this is a warning message')
logger.error('this is an error message')

import logging.config

logging.config.fileConfig('logging.conf')

logger = logging.getLogger('simpleExample')
print()
print()
logger.debug('this is a debug message')


# stack trace 
import logging
import traceback

try:
    a = [1,2,3]
    val = a[4]
#except IndexError as e:
#    logging.error(e, exc_info=True)
# or can use:
except:
    logging.error("The error is %s", traceback.format_exc())
# this give the same error message as previous code.


#Rotating file handlers
#from logging.handlers import RotatingFileHandler

#logger = logging.getLogger(__name__)
#logger.setLevel(logging.INFO)

#handler = RotatingFileHandler('app.log', maxBytes=2000, backupCount=5)
#logger.addHandler(handler)

#for _ in range(10000):
#    logger.info("Hello, world!") Creates 5 2kb files with hello wold written in it.

from logging.handlers import TimedRotatingFileHandler
import time

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# s, m, h, d, midnight, w0=Monday, w1=Tuesday, etc for the when attribute
handler = TimedRotatingFileHandler('timed_test.log', when='m', interval=1, backupCount=5)
logger.addHandler(handler)

for i in range(6):
    logger.info("Hello, world!")
    time.sleep(50)


print()
done = input("are you done looking at results, hit enter")
