"""What is decorator?
Decorator allows us to wrap another function in order to extend
the behaviour of wrapped function without modifying behaviour of it
"""

def mult(func):
    def wrapper():
        x = func()
        return x*x
    return wrapper

@mult
def num():
    return 10
print(num())

"""
Monkey patching refers to matching or updating piece of code or any module 

*args = args is used to pass the variable number of argument to a function
**kwargs = kwargs is used to pass a variable length argument
"""




def sum(a, b):
    return a+b

# decorate a function to give (a+b)*10
def summ(func):
    def wrapper():
        a, b = func()
        return (a+b)*10
    return wrapper

@summ
def sm():
    return 1, 2
print(sm())





def arg_func(*args):
    for i in args:
        print(i)
arg_func("vandana","gajendra","prathibha")


def kwargs_func(**kwargs):
    print(kwargs)
kwargs_func(first = 6, second =5)
