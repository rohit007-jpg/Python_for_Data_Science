'''
    This is a test module named example which is used to see how exactly modules work in python 
    and how we can use them by importing to our program. 
    Here, we define function named ---> add(x,y), mul(x,y) and fact(num)
    
'''

def add(x,y):
    '''
    function "add" takes two arg "x" and "y" and returns "x+y". This is it.
    '''
    return x+y;

def mul(x,y):
    '''
    function "mul" takes two arg "x" and "y" and return "x*y"
    '''
    return x*y;

def fact(num):
    '''
    function fact takes "num" as an arg and return the factorial of that number 
    '''
    return 1 if num==1 else num*fact(num-1);



