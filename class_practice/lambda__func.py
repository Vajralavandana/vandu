"""
a lambda can take any num of argument but can only have one expression
"""
x = lambda a: a + 5
print(x(10))

def add_5():
    return lambda a : a+5

b = add_5()
print(b(5))

y = lambda a, b: a * b
print(y(3, 4))

def mult():
    return lambda a, b: a*b

a = mult()
print(a(3,4))

def func(n):
    return lambda a: a * n

z = func(6)
print(z(4))


def add(n):
    return n + n


num = (2, 7, 8, 9)
res = map(add, num)
print(list(res))

numbers = (5, 7, 8)
res = map(lambda x : x + x, numbers)
print(list(res))

num_a = [2, 9, 8, 7]
num_b = [5, 1, 3, 6]
research = map(lambda x, y : x + y, num_a, num_b)
print(list(research))

num = [5, 7, 8, 2, 4, 10, 1, 3, 22, 6]
fil_eve = filter(lambda a: a % 2 == 0, num)
fil_odd = filter(lambda a: a % 2 != 0, num)
print("filtered even numbers are:{}".format(fil_eve))
print("filtered odd numbers are:{}".format(fil_odd))

z = lambda x: True if x < 10 else False
print(z(2))
print(z(11))