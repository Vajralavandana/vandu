"""
what is tuple?
tuple is group of elements which can be alphabets, numbers and alphanumeric or combinations of all which is represented between small braces

***tuple is immutable
"""

"""
difference between list and tuple

list                                                   tuple
1 list is mutable                              1 tuple is immutable
2 list can be appended and extended            2 tuple cannot be appended or extended
3 list allocated extra memory and space        3 tuple allocated memory space only for declared elements
"""

"""
why list is slow than tuple?
during runtime it checks for all the memory space allocated for list where list has extra memory space, hence list is slow and tuple doesnot have extra space allocate hence tuple is fast

"""

#one way of declaring tuple
emp_tup = ()
print("the value of empty tuple is {}".format(emp_tup))

#another way of creating tuple
emp_tup = tuple()
print("the another way of creating empty tuple is {} ".format(emp_tup))

tpl= (1,"a", "python@3")
print("the value of tuple is {}".format(tpl))