# # write a function to get the descending order of the list
# list = [3, 10, 0, 50, 2, 48]
# list.sort()
# print("the value of list after sorting is {}".format(list))
#
# list.reverse()
# print("the value of list after reversing is {}".format(list))
#
# def descending_list(list):
#     list.sort()
#     list.reverse()
#     return list
#
# list = descending_list([3, 5, 1, 0])
# print(list)
#
# def des_list(list):
#     list.sort()
#     rev_list = []
#     for i in list:
#         rev_list = i + rev_list
#     return rev_list
#
# a = des_list([5, 7, 2, 1])
# print(a)
#
# #write a method to list type of values in dictionary
# dict_a = {"a": 1, "b": "2"}
# # get_values = dict_a.values()
# # print(get_values)
# # type_get_values = type(get_values)
# # print(type_get_values)
# type_dict_a = type(dict_a["a"])
# print(type_dict_a)
# type_dict = type(dict_a["b"])
# print(type_dict)
# print("the type of dict_a of a is {}, the type of dict_a of b is {}".format(type_dict_a, type_dict))
#
# def type_dict(dict):
#     dict1 = { }
#     for i in dict:
#         dict1 = type(dict_a[i])
#         return dict1
#
# dict_a_type1 = type_dict({"a":1})
# print(dict_a_type1)

lst = [3, 5, 1, 99, 2, 0]
lst.sort()
print("List after sorting  {}".format(lst))
desc_lst = []
for i in lst:
    # desc_lst.insert(0, i)
    desc_lst = [i]+desc_lst
print("descending order of list is {}".format(desc_lst))

def desc_lst(list):
    list.sort()
    desc_list = []
    for i in list:
        desc_list = [i] + desc_list
    return desc_list

q = desc_lst([5, 3, 7, 6, 90])
print("the value of descending list is {}".format(q))
a= desc_lst([1, 8, 3, 99, 78, 100, 200, 600, 250])
print("the value of descending list is {}".format(a))

# type of values in dict
dicta = {"a": 1, "b": "2"}
val_typ = []
for key, val in dicta.items():
    val_typ.append(type(val))
print("The type of values in dictionary is {}".format(val_typ))

lm = [type(j) for i, j in dicta.items()]
print(lm)

def dicta(dict):
    val_typ = []
    for key, val in dict.items():
        val_typ.append(type(val))
    return val_typ
x = dicta({"p": 1, "q":"5"})
print(x)
y = dicta({"d":6, "e":5})
print(y)