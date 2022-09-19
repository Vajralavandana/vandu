"""
what is list?
List is a group of elements which can be alphabets, numbers and alphanumeric or combinations of all which is represented between square braces.
*** List is mutable
"""

# declaring empty list
empty_lst = []
print("type 1 declaration of empty list is {}".format(empty_lst))

# another way of declaring empty list
emp_lst = list()
print("type 2 of declaringempty list is {}".format(emp_lst))


lst = [1, "a", "@", "10", "python@3"]
print("The value of list is {}".format(lst))
type_lst = type(lst)
print("The type of variable lst is {}".format(type_lst))

#Appending in list   (only single element can be appended)
lst.append("vandana")
print("the value of list after appending is {}".format(lst))

#Extending in list      (only list of elements can be extended)
ext_lst = ["lokesh", "abc"]
lst.extend(ext_lst)
print("the value of list after extending is {}".format(lst))

lst_x = ["a", "b", "c"]
zer_ind_lst_x = lst_x[0]
print("The value of zeroeth index of list is {}".format(zer_ind_lst_x))
frst_ind_lst_x = lst_x[1]
print("The value of first index of list is {}".format(frst_ind_lst_x))
scd_ind_lst_x = lst_x[2]
print("The value of second index of list is {}".format(scd_ind_lst_x))