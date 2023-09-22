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


