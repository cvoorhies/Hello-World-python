"""
Difference between arguments and parameters
   - Arguments are:
   - Parameters are:

Positional and keyword arguments

Variable-length Arguments (*args and **kwargs)

Container unpacking into a function arguments

Local vs global arguments

parameter passing (by value or by reference?)
"""
def greeting(name): #name is a parameter
    print(f"Welcome to the world, {name}")


greeting("Clyde") # Clyde is an argument

#Positional arguments:
def foo(a, b, c, d=4): #d is a default value
    print(a, b, c, d)

foo(1, 2, 3)
foo(c=1, b=2, a=3) #key/value arguments Positional place matters when using this way
#the Keyords position matters, not the value.

def foobar(a, b, *args, **kwargs): 
    # If you mark a parameter with one *, then you can pass any number of position arguments to your function
    # If you mark a parameter with two * then you can pass any number of keyword arguments to the function
    # args is a tuple.
    print(a,b)
    for arg in args:
        print(arg)
    # **kwargs is a dictionary.
    for key in kwargs:
        print(key, kwargs[key])
    
foobar(1, 2, 3, 4, 5, six=6, seven=7)

#enforcing 

def foo2(a, b, *, c, d):
    print(a, b, c, d)

foo2(1, 2, c=3, d=4)

def foo3(*args, last):
    for arg in args:
        print(arg)
    print(last)
    
foo3(1, 2, 3, last=100)

#Unpacking arguments
def foo4(a, b, c):
    print(a, b, c)
    
my_list= [0, 1, 2] # also works with a tuple
foo4(*my_list)


def foo5(a, b, c):
    print(a, b, c)
    
my_dict= {'a': 5, 'b': 6, 'c': 7} # Key words must match args in function.
foo5(**my_dict)


"""Passing parameters, call by value or call by reference
The parameter parsed in is actually a reference to an object, but the reference
is passed by value.
There is a difference between mutable and immutable data types.
""" 
"""
Astrisk Operator
It can be used for multiple differnt cases like multiplication and power operations,
the creation of lists or tuples, with repeated eleents, for args, kwargs, and keyword
only parameters for unpacking lists, tuples, or dictionaries into function arguments, 
for unpacking containers and for merging containers into a list or merging two
dictionaries.

"""
result = 2 ** 4 #double * is for power operations
print(result)

zeros = [0] * 10 #for filling a list
print(zeros)


# used to unpack lists and tuples. * result is always going to be a list.
numb_list = [1, 2, 3, 4, 5, 6]
beginning, *middle, secondlast, last = numb_list
print(beginning)
print(middle)
print(secondlast)
print(last)

# can use * operator to merge iterables into a list
my_tuple = (1, 2, 3)
my_list = [4, 5, 6]
my_set = {7, 8, 9}

new_list = [*my_tuple, *my_list, *my_set]
print(new_list)

dict_a = {'a': 1, 'b': 2}
dict_b = {'c': 3, 'd': 4}

my_new_dict = {**dict_a, **dict_b}
print(my_new_dict)

#Deep vs Shallow copying. Shallow is just a regular copy of the item
#Deep copy is for multi layers of objects
import copy
org =[[1, 2, 3, 4], [5, 6, 7, 8, 9]]
cpy = copy.deepcopy(org) # if you use just copy it copies the reference not the actual object
cpy[0][1] = -10

print(cpy)
print(org)

# Context Managers
"""
Great tool for resource managment, they allow you to allocate and release resources
precisely when you want to. A well know example is the with open statement.
"""
# open a file 
with open('notes.txt', 'w') as file: # this is the recommened way to open files.
    file.write('Some todo list....')
#Context manager with automaticlly close the file once code is outside the with.
# to free up resources correctly:

file = open('notes.txt', 'a')
try:
   file.write('some todo lists...')
finally:
    file.close()

from threading import Lock
lock = Lock()

lock.acquire()
###--- some threading code. 
lock.release()# if you forget this part the program won't run any further.

#a better and cleaner way to do this that will automatically release is to use:
with lock:
    #.. some threading code
    print('this is the lock code')

class ManagedFile:
    def __init__(self, filename):
        print('init')
        self.filename = filename
    
    def __enter__(self):
        print('enter')
        self.file = open(self.filename, 'w')
        return self.file
    
    def __exit__(self, exc_type, exc_value, exc_traceback):
        if self.file:
            self.file.close()
            print('exc: ', exc_type, exc_value)
            print('exit')

with ManagedFile('note.txt') as file:
    print('do something here')
    file.write('some todoos....')

# opening file with a function:
from contextlib import contextmanager

@contextmanager # the decorator
def open_managed_file(filename):
    f = open(filename, 'w')
    try:
      yield f # This is the generator
    finally:
      f.close()

with open_managed_file('anotherNoteFile.txt') as f:
    f.write('Some text inside the file...')