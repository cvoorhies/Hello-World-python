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


