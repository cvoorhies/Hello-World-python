# functions needed
# input variables
# loop function to get inputs
addSum = lambda x,y: x + y
subSum = lambda x,y: x - y
multiSum = lambda x,y: x * y
divSum = lambda x,y: x / y

a_input = input('input first number: ')
oper_sign = input("input oprator: ")
b_input = input('input second number: ')
if oper_sign == '+':
    result = addSum(float(a_input), float(b_input))
    print (result)
elif oper_sign == '-':
    result = subSum(float(a_input), float(b_input))
    print (result)
elif oper_sign == '*':
    result = multiSum(float(a_input), float(b_input))
    print (result)
elif oper_sign == '/':
    if b_input == '0':
        print("Cannot divide by 0")
    else:
        result = divSum(float(a_input), float(b_input))
        print (result)