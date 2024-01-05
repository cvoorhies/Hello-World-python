#functions
def hello():
    print('Hello world again!!!')

def factorial(n):
    """ this is a docstring used to annotate what programs are doing and utilize
    the help to get more information about it.This function will give you the factorial of a number
    """
    if n==1 : return 1
    #print(n)
    return n * factorial(n-1)
    