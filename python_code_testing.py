
# Python program to illustrate isdigit()
# string with all digits
s = '123'
print(s.isdigit())

# string with digits and whitespaces
s = '123 567'
print(s.isdigit())

# string with alphabets and digits
s = 'Hello500'
print(s.isdigit())

# string with floating-point number
s = '10.42'
print(s.isdigit())

# string with separator
s = '10,20,500'
print(s.isdigit())

# empty string
s = ''
print(s.isdigit())