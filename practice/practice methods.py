# write a method to sum of all elements in list
# write a method to find cubes of elements in list

a = [1, 2, 3, 4, 5]
sum_a = 0
for i in a:
    sum_a = i + sum_a
print(sum_a)

def lst_a(list):
    sum_a = 0
    for i in list:
        sum_a = i + sum_a
    return sum_a

a = lst_a([1, 2, 3, 4, 5])
print("the sum of list is {}".format(a))
b = lst_a([10, 20, 30])
print("the sum of list is {}".format(b))

c = [1, 2, 3, 4]
cube_c = []
for i in c:
    cube_c.append(i*i*i)
print(cube_c)

def cube(list):
    cube_c = []
    for i in list:
        cube_c.append(i*i*i)
    return cube_c

x = cube([1, 2, 3, 4])
print("the cube values of list are {}".format(x))

y = cube([5, 6, 7, 8])
print("the cube values of list are {}".format(y))

#square
d = [1, 2, 3, 4]
squ = []
for i in d:
    squ.append(i*i)
print(squ)

def squ_d(list):
    squ = []
    for i in list:
        squ.append(i*i)
    return squ

p = squ_d([1, 2, 3, 4, 5])
print("the square values of list are {}".format(p))

q = squ_d([6, 7, 8, 9, 10])
print("the square values of list are {}".format(q))