# functions needed
# input variables
# loop function to get inputs
a_input = 0.00
b_input  = 0.00
oper_sign = '+'
a_input = input('input first number: ')
oper_sign = input("input oprator")
b_input = input('input second number: ')
if oper_sign == '+':
    #a_input = float(a_input)+ float(b_input)
    #print (a_input)
    result = int(lambda a_input,b_input: a_input+b_input)
    print(result)
elif oper_sign == '-':
    a_input = float(a_input)- float(b_input)
    print (a_input)
elif oper_sign == '*':
    a_input = float(a_input)* float(b_input)
    print (a_input)
elif oper_sign == '/':
    if b_input == '0':
        print("Cannot divide by 0")
    else:
        a_input = float(a_input)/ float(b_input)
        print (a_input)