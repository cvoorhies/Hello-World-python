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

inputList = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41.0], ['Harsh', 39.0]]

#print(inputList)
n = len(inputList)
i = 0 
j = 1 
whoISsecPlace1 = ''
whoISsecPlace2 = ''
def Second_Place(arr):
    lowest = 100.00
    secPlace1 = arr[0][1]
    secPlace2 = arr[1][1]
    max = 0
    if n < 2:
        return n
    else:
        #Find the lowest value in the list
        for i in range(n):
            if lowest > arr[i][1]:
                lowest = arr[i][1]
        #print(lowest) 
        for i in range(n):
            if max < arr[i][1]:
                max = arr[i][1]
        print(lowest, max)
        #find the second lowest in the list and repeat if there are more than one.       
        for i in range(n):
            if arr[i][1] >= lowest and arr[i][1] < max:
                secPlace1 = arr[i][1]
                #print(secPlace)
                whoISsecPlace1 = arr[i][0]
            if arr[i][1] < secPlace2 and secPlace2 != lowest:
                secPlace2 = arr[i][1]
                whoISsecPlace2 = arr[i][0]
    return secPlace1, whoISsecPlace1, secPlace2, whoISsecPlace2   

print(Second_Place(inputList))
