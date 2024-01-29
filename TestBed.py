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
print (origList)"""

