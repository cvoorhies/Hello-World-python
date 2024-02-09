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

#MyList = [['Harry', 37.21], ['Berry', -37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
#MyList = [['Prashant', 36], ['Pallavi', 40], ['Dheeraj', 40], ['Shivam', 40]]
#MyList = [['Prashant', 32], ['Pallavi', 36], ['Dheeraj', 39], ['Shivam', 40]]
MyList = [['Rachel', -50], ['Mawer', -50], ['Sheen', -50], ['Shaheen', 51]]

n = len(MyList)

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
    
    
Second_Place(MyList)
