"""import itertools

n=5
mystring = []
for i in range(n):
    mystring.append(i+1)
    n -= 1
    i += i
    
newstring = ''.join(str(e) for e in mystring)
print(newstring)

#list comprehensions!
x = 1
y = 1
z = 2
n = 3
#i=0
def find_valid_coordinates(x, y, z, n):
    valid_coords = []
    for i in range(x+1):
        for j in range(y+1):
            for k in range(z+1):
                if i + j + k != n:
                    valid_coords.append([i,j,k])
    return valid_coords

origList = find_valid_coordinates(x, y, z, n)
print (origList)

x = 1
y = 1
z = 2
n = 3
empty_coords = []
def find_valid_coordinates(x, y, z, n):
    valid_coords = []
    for i in range(x+1):
        for j in range(y+1):
            for k in range(z+1):
                if i + j + k != n:
                    valid_coords.append([i,j,k])
    return valid_coords

origList = find_valid_coordinates(x, y, z, n)
# invalid syntax : newList = [empty_coords.append([i]) + empty_coords.append([j]) + empty_coords.append([k])  for i in range(x+1), for j in range(y+1), for k in range(z+1) if i + j + k != n]
print (origList)
#print(newList)"""

"""n=4
arr = [57,57,57,-57]
newList = list(arr)
newList.sort()

if n != len(newList):
    n = len(newList)
    
def Second_Place(arr):
    max = -100
    secPlace = -100
    if n < 2 or n > 10:
        return n
    else:
        for i in range(len(arr)):
            if arr[i]<= -100 or arr[i] >100:
                return arr[i]
        for i in range(n):
            if max < arr[i]:
                max = arr[i]
        for i in range(n):
            if arr[i] < max or arr[i] < secPlace:
                secPlace = arr[i]
    return secPlace     

print(Second_Place(newList))"""

MyList = [['Harry', 37.21], ['Berry', -37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
#MyList = [['Prashant', 36], ['Pallavi', 40], ['Dheeraj', 40], ['Shivam', 40]]
#MyList = [['Prashant', 32], ['Pallavi', 36], ['Dheeraj', 39], ['Shivam', 40]]
#MyList = [['Rachel', -50], ['Mawer', -50], ['Sheen', -50], ['Shaheen', 51]]

"""n = len(MyList)

j = 1 

def Second_Place(arr):
    whoISsecPlace1 = 'Default Person1'
    lowest = 100
    secLowest = -1
    max = 0
    i = 0 
    NewList = []
    for i in range(n):  
        if (max < arr[i][1]):            
            max = arr[i][1]
            
    for i in range(n):
        if lowest > arr[i][1]:
            lowest = arr[i][1]
            secLowest = arr[i+1][1]
            if secLowest == lowest and secLowest < max:
                    secLowest = max
            
    for i in range(n):
        if arr[i][1] < max or arr[i][1] > lowest and secLowest != lowest:
            if arr[i][1] > lowest and arr[i][1] < secLowest:
                secLowest = arr[i][1]
                
    
    print(lowest, secLowest, max)
#find the second lowest in the list and repeat if there are more than one.  
    for i in range(n):
        if arr[i][1] == secLowest:
            NewList.append([arr[i][0]])
            NewList.sort()
           
    for i in range(len(NewList)):
            whoISsecPlace1 = NewList[i][0]
            print(whoISsecPlace1) 
    
    
Second_Place(MyList)"""

"""#n = 3
#my_Dict = {'Krishna': [67.0, 68.0, 69.0], 'Arjun': [70.0, 98.0, 63.0], 'Malika': [52.0, 56.0, 60.0]}

n = 2
my_Dict = {'Harsh': [25, 26.5, 28], 'Anurag' : [26, 28, 30]}


query_name = 'Harsh'

results = my_Dict.get(query_name)
print(results)

new_list = 0.0
for i in range(3):
    new_list = (results[i] + new_list)

print("%.2f" % (new_list/3))"""


# these two lists are the "input()" from the hacker rank challenge to make the following seg of code work.
#['insert 0 5', 'insert 1 10', 'insert 0 6', 'print', 'remove 6', 'append 9', 'append 1', 'sort', 'print', 'pop', 'reverse', 'print']
#[29, 'append 1', 'append 6', 'append 10', 'append 8', 'append 9', 'append 2', 'append 12', 'append 7', 'append 3', 'append 5', 'insert 8 66', 'insert 1 30', 'insert 6 75', 'insert 4 44', 'insert 9 67', 'insert 2 44', 'insert 9 21', 'insert 8 87', 'insert 1 75', 'insert 1 48' ,'print', 'reverse', 'print', 'sort', 'print', 'append 2', 'append 5', 'remove 2', 'print']

# This code takes input from the keyboard. type in the commands from the above list and it works.
"""arr = []
for _ in range(12):
    command, *args = input().split() #splits up the commands and arguments, expects input from keyboard
    if command != 'print': # looks to see if the command is not print
        getattr(arr, command)(*map(int, args)) #the use of the getattr function is to dynamically access an attribute or method of an object called ar. 
        # the * unpacks the map function output into seperate int. the map function takes two arguments, the first is a function the second is an iterable (i.e. a list, a tuble, etc).  
    else:
        print(arr)"""

"""n = int(input())
integer_list = map(int, input().split())
    
print(str(integer_list))"""
"""for val in integer_list:
    values = map(str, val)
    print(hash(values))"""


"""def count_substring(string, sub_string):
    count = 0
    for i in range(len(string)-len(sub_string)+1):
        t = string[i:]
        if t.startswith(sub_string):
            count += 1
    return count

count = count_substring("abcdcdc", "cdc")
print(count)"""

"""s = "qA2"
    
print(any([str.isalnum(i) for i in s]))
print(any([str.isalpha(i) for i in s]))
print(any([str.isdigit(i) for i in s]))
print(any([str.islower(i) for i in s]))
print(any([str.isupper(i) for i in s]))"""


"""thickness = int(11) #This must be an odd number 
filler_leters = 'H'
for i in range(thickness): 
    print((filler_leters*i).rjust(thickness-1)+filler_leters+(filler_leters*i).ljust(thickness-1))
for i in range(thickness+1): 
    print((filler_leters*thickness).center(thickness*2)+(filler_leters*thickness).center(thickness*6))
for i in range((thickness+1)//2): 
    print((filler_leters*thickness*5).center(thickness*6))
for i in range(thickness+1): 
    print((filler_leters*thickness).center(thickness*2)+(filler_leters*thickness).center(thickness*6))
for i in range(thickness): 
    print(((filler_leters*(thickness-i-1)).rjust(thickness)+filler_leters+(filler_leters*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))"""

"""def print_formatted(number):
    # your code goes here
        # your code goes here
    width = len(bin(number)[2:])
    for i in range(1, number+1):
        dec = str(i).rjust(width)
        oct_num = oct(i)[2:].rjust(width)
        hex_num = hex(i)[2:].rjust(width).upper()
        bi_num =  bin(i)[2:].rjust(width)
        print(f"{dec} {oct_num} {hex_num} {bi_num}")


n = 17
print_formatted(n)"""

