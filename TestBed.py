import itertools

"""n=5
mystring = []
for i in range(n):
    mystring.append(i+1)
    n -= 1
    i += i
    
newstring = ''.join(str(e) for e in mystring)
print(newstring)"""

x = 1
y = 1
z = 2
n = 3

mystring1 = [x, y, z]
#mystring2 = [0, 0]
#mystring3 = [0, 0]
#0<=i<=x, 0<=j<=y, 0<=k<=z

print([[0<=x<=x, 0<=y<=y, 0<=z<=z] for x in range(1,n+1)])

#print (mystring1)


origList = [[0,0,0],[0,0,1],[0,0,2],[0,1,0],[0,1,1],[0,1, 2],[1, 0,0],[1,0,1],[1,0,2],[1,1,0],[1,1,1],[1,1,2]]
i=0
myCombo = list(itertools.permutations(mystring1, n))
myCombo = list(itertools.combinations(myCombo, n))
#print(myCombo)