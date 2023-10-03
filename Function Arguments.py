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