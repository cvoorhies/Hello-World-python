import json
from typing import Any

#Serialization or Encoding
person = {"name": "John", "age": 30, "city":"New York", "hasChildren": False, "titles": ["engineer", "programmer"]}

personJSON = json.dumps(person, indent=4, sort_keys=True)
#print(personJSON)

#with open('person.json', 'w') as file:
#    json.dump(person, file, indent=4)

#*********** deserialization or decoding
#person = json.loads(personJSON)
#print(person)

with open('person.json', 'r') as file: 
    person = json.load(file)
   # print(person)

###***** from a class to a JSON file

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

user = User('Max', 27)

def encode_user(o):
    if isinstance(o, User):
        return {'name': o.name, 'age': o.age, o.__class__.__name__ : True}
    else:
        raise TypeError('Object of type User is not JSON serializable')

##Another way to do this is with the json library
# Encoding and decoding custom classes

from json import JSONEncoder
class UserEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, User):
            return {'name': o.name, 'age': o.age, o.__class__.__name__ : True}
        return JSONEncoder.default(self, o)

userJSON = UserEncoder().encode(user)
#userJSON =json.dumps(user, cls=UserEncoder) or use default=encode_user gives the same result
print(userJSON)

user2 = json.loads(userJSON)
print(user2)

def decode_user(dct): # decodes it back to a user class so you can access the user.name or user.age
    if User.__name__ in dct:
        return User(name=dct['name'], age=dct['age'])
    return dct

user2 = json.loads(userJSON, object_hook=decode_user)
print(user2.name)

#### Random numbers

import random

a = random.random() #prints randome float numb between 0 and 10
print(a)
a = random.uniform(1, 10) #prints randome float numb between 1 and 10
print(a)
a = random.randint(1, 10) #prints randome int numb between 1 and 10
print(a)
a = random.normalvariate(0, 1) #prints randome int numb between mu and sigma. good for statistics
print(a) # mu = mean, sigma = std deviation, normal distribution.

#Random sequences
mylist = list("ABCDEFGH")
a = random.choice(mylist)
print(a) # picks random choice in list

mylist = list("ABCDEFGH")
a = random.sample(mylist, 3) # of samples to pick
print(a) # picks random choice in list

mylist = list("ABCDEFGH")
a = random.choices(mylist, k=3) # of samples to pick, will pick multiple of the same item
print(a) # picks random choice in list

mylist = list("ABCDEFGH")
random.shuffle(mylist) # shuffles the list as in the poker game
print(mylist) 

# Randome.seed(#) will give you repeatable results.

import secrets # has only 3 functions, used for passwords, tolkens, or account verifications, etc.

a = secrets.randbelow(10) #does not include 10
print(a)

a = secrets.randbits(4) #dgive randome bianary values between 0000 and 1111, returns an int
print(a)

mylist = list("ABCDEFGH")
a = secrets.choice(mylist) #dgive randome bianary values between 0000 and 1111, returns an int
print(a)

#use the numby to gennerate random arrays of various depths
import numpy as np

a = np.random.rand(3) # creates a 1d 3 element array
print(a)

a = np.random.rand(3, 3) # creates a 3d 3 element array
print(a)

a = np.random.randint(0, 10, (3,4)) # creates a 3d 3 element int array ()=tuplel
print(a)

arr = np.array([[1,2,3], [4,5,6], [7,8,9]])
print(arr)
np.random.shuffle(arr) # shuffles only in the first axis
print(arr)

np.random.seed(1)
print(np.random.rand(3,3))

np.random.seed(1)
print(np.random.rand(3,3))# generates the same random numb array as the first

### Decorators - 2 types are function decorators and class decorators

"""
Basic syntac of a decorator
@mydecorator
def dosomething():
    pass

It's a function that takes a function as an argument that extends the functionability

"""
## Template for a decorator:
import functools
def my_decorator(func):

    @functools.wraps(func)
    def wrapper(*args, **kwargs): # *args, **kwargs allows an unlimited amount of arg to be passed
        #Do something
        result = func(*args, **kwargs)
        #Do something else
        return result
    return wrapper

@my_decorator
#def print_name():
#    print('Clyde')

#print_name = start_end_decorator(print_name)

#print_name()

def add5(x):
    return x + 5

result = add5(10)
print(result)

print(help(add5))
print(add5.__name__)


### another example of a decorator
def repeat(num_times):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator_repeat

@repeat(num_times=4)
def greet(name):
    print(f'Hello {name}')

greet('Clyde')


## Stack decorators ontop of each other, or nested decorators

def start_end_decorator(func):

    @functools.wraps(func)
    def wrapper(*args, **kwargs): # *args, **kwargs allows an unlimited amount of arg to be passed
        print('Start functools wrapper')
        result = func(*args, **kwargs)
        print('End functools wrapper')
        return result
    return wrapper

def debug(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
        signaure = ", ".join(args_repr + kwargs_repr)
        print('Start debug wrapper')
        print(f"Calling {func.__name__}({signaure})")
        result = func(*args, **kwargs)
        print(f"{func.__name__!r} return {result!r}")
        print('End debug wrapper')
        return result
    return wrapper

@debug
@start_end_decorator
def say_hello(name):
    greeting = f'Hello {name}'
    print(greeting)
    return greeting

say_hello("Clyde")

### Class decorators, used to maintain and update a state

class CountCalls:

    def __init__(self, func):
        self.func = func
        self.num_calls = 0

    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print(f'This is executed {self.num_calls} times')
        return self.func(*args, **kwargs)



@CountCalls
def say_hello():
    print('Hello World')

say_hello()
say_hello()
say_hello()
say_hello()

# Typical use cases of decorators

"""
Impliment a timer decorator to calculate the execution time of a function
use debug: to print out more information about a called function and its arguments
use a check decorator to check if the arguments fulfill some requirements and the depth 
the behavior accordingly
register functions, like plug ins, with decorators, you can cache the return values
you can add information or update the state generators or functions that return 
an object that can be iterated
"""

## Generators
"""
Generators are functions that return an object that can be iterated over. And the
special thing is that they generate the items inside the object lazily,  which means
they generate the items only one at a time and only when you ask for it. 
And because of this,  they are much more memory efficient than other sequence objects
when you have to deal with large data sets. They are a powerful advanced python
technique. 
"""

def mygenerator():
    yield 1
    yield 2
    yield 3

g = mygenerator()
print(g)

"""
for i in g:
    print(i)
"""

"""value = next(g)
print(value)

value = next(g)
print(value)

value = next(g)
print(value)

"""

#print(sum(g))

print(sorted(g))

def countdown(num):
    print('Starting')
    while num > 0:
        yield num
        num -= 1

cd = countdown(4)

value = next(cd)
print(value)

print(next(cd))
print(next(cd))
print(next(cd))

# Generators are very memory efficient, they save a lot of memore when working
# with large data


import sys
def firstn(n):
    nums = []
    num = 0
    while num < n:
        nums.append(num)
        num += 1
    return nums

def firstn_generator(n):
    num = 0
    while num < n:
        yield num
        num += 1


#print(firstn(10))
print(sys.getsizeof(firstn(100000)))
print(sys.getsizeof(firstn_generator(100000)))

def fibonacci(limit):
    # 0,1,1, 2, 3, 5, 8, 13...
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b


fib = fibonacci(35) # doesn't include the value indicated
for i in fib:
    print(i)


"""
Generator expressions: written the same way, like list comprehensions, but with
parentheses instead of square bracket. This is a very simple and shortcut to immplement
the generator expression.

"""
mygenerator2 = (i for i in range(10) if i % 2 == 0)
#for i in mygenerator2:
#    print(i)
    
print(list(mygenerator2))

# list comprehension:
mylist2 = [i for i in range(10) if i % 2 == 0]
print(mylist2)

print(sys.getsizeof(mygenerator2))
print(sys.getsizeof(mylist2))

"""
Threading vs multiprocessing: Threading and multiprocessing, you can run code in 
parallel and speed up your code. The differences between a process and a thread, 
the advantages and disadvantages of both how and why threads are limited by the Gil
and how we can easily use the built in threading and multiprocessing module to create
and run multiple threads or processes.
"""
# The difference between a process and a thread. So a process is an instance of a 
# program.
"""
so for example,  if I'm running on Firefox browser,  then this is and instnce of a
program. So for if I'm running one Firefox browser,  then this is one process. Or if
I'm running one Python interpreter, then this is one process. And a thread on the 
other hand is an entity within a process. So a process can have multiple threads
inside processes that takes advantage of multiple CPUs and cores. So you can execute
your code on multiple CPUs and parallel processes have a separate memory space. So
Memory is not shared,  but between processes and they are great for CPU bound processing.
So this means for example, if you have a large amount of data and have to do a lot
of expensive computations for them, then with multiprocessing, you can process the
data on different CPUs and this way speed up your code. New process is started
independently from other processes and processes are easily interruptible and killable
There is one GIL for each process. So this avoinds the Gil limitation. * Gil, Global
interpreter lock.* 
There are some disadvantages. A process is heavyweight. It takes a lot of memory
and starting a process is slower than starting a thread. Since processes have a separate 
memory space, memory sharing is not so easy. So the interprocess communication is more 
complicated.

A thread is an entity within a process that can be scheduled for execution. It's also
known as a lightweight process. A process can spawn multiple threads. So all threads
within a process share the same memory. Starting a thread is faster than starting a 
process. They are great for IO bound tasks. So this means input output tasks. For
example when your program has to talk to slow devices, like a hard drive or a network
connection, then with threading, your program can use the time waiting for these devices
and then intelligently switch to other thread and do other processing. So this is how 
you can speed up code with threading. 

But on the other hand, threading is limited by the Gil. So the Gil allows only one thread
at a time. So there is no actual parallel computation in multithreading. So threading 
has no effect for CPU bound tasks. And they are not interuptable and killable. So
be careful with memory leaks here. Since threads share the same memory you have to be
careful with race conditions. A race condition occurs when two or more threads want to
modify the same variable at the same time. So then this can easily cause bugs or crashes

GIL : Global interpreter Lock. This is a lock in python that allows only one thread
at a time to execute. This is very controversial in the python community. But why is
it needed? This is because in C Python, so C Python is the reference python implementation
that you get when you download and install python fro python.org.
So the GIL is needed because in C Python, there is a memory management that is not 
thread safe. So in C Python,  there is a technique that is called reference counting
that is used for memory management. And this means that objects created in Python have
a reference count variable that keeps track of the number of references that point to
the object. When this cound reaches zero, the memory occupied by the object can be 
released. The problem now in multi threading is that this reference count variable 
needs protection from race conditions where two threads increase or decrease the 
value simultaneously. So if this happens it can cause leaked memory that is never released
Or it can incorrectly release the memory while a reference to that object still exists.
So this is the reason why they introduced the GIL. A couple of ways to avoid the GIL
if you want to use parallel computing is to use multi processing. Or you can use a
different fre threaded Python implementation and not C Python. For example, Chai Thon
or iron Python. Or you can use Python as a wrapper for third party libraries. Thi is
the way it works in NumPy or the scipy modules. So they are basically just wrappers
in Python, that then calls code that is executed in C. 
"""