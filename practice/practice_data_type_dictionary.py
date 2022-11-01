emp_dict = dict()
print("the one way of diclaring empty dictionary is {}".format(emp_dict))

emp_dict1 = {}
print("the another way of diclaring empty variable is {}".format(emp_dict1))

dict1 = dict()
dict1["Name"] = "alex"
dict1["age"] = 25
dict1["salary"] = 20000
print("the value of dictionary is {}".format(dict1))

len_dict1 = len(dict1)
print("the length of dictionary is {}".format(len_dict1))

type_dict1 = type(dict1)
print("the type of dictionary is {}".format(type_dict1))

dict1.update({"empid" : 1})
print("the value of dictionay after updating is {}".format(dict1))

# another way
dict2 = {"a": 1, "b": 2, "c": 3}
print("the value of dictionary is {}".format(dict2))

dict2.update({"d": 4, "e": 5})
print("the value of dict after updating is {}".format(dict2))

# get key value
get_ele = dict1["age"]
print("the value of age is {}".format(get_ele))
get_elem = dict2["b"]
print("the value of b is {}".format(get_elem))

get_ele1 = dict1.get("salary")
print("the value of salary is {}".format(get_ele1))

get_element =dict2.get("a")
print("the value of a is {}".format(get_element))

#fetch keys from dictionary
get_keys = dict1.keys()
print("the value of keys is {}".format(get_keys))

#fetch values
get_values = dict1.values()
print("the values are {}".format(get_values))

get_values1 = dict2.values()
print("the values of dict2 is {}".format(get_values1))

get_values = list(dict1.values())
print("the values of dict1 in list is {}".format(get_values))
get_values1 = list(dict2.values())
print("the values of dict2 in list is {}".format(get_values1))

#get items
get_item = dict1.items()
print("the items of dict are {}".format(get_item))
get_item1 = list(dict1.items())
print("the items of dict in list are {}".format(get_item1))

#pop and popitem
pop_key_value = dict2.pop("a")
print("the value of dict after popping is {}".format(dict2))
pop_key_value1 = dict1.pop("age")
print("the value of dict after popping is {}".format(dict1))

pop_item = dict1.popitem()
print("the value of dict after popping is {}".format(dict1))

pop_items = dict2.popitem()
print("the value of dict after popping is {}".format(dict2))

clear_dict = dict1.clear()
print("the value of dict after clearing is {}".format(clear_dict))

lst1 = ["vegetables", "fruits"]
lst2 = [["beans", "carrot"], ["apples", "orange"]]
dict3 = dict(zip(lst1, lst2))
print("the value of dict from 2 lists is {} ".format(dict3))

dict3.update({"vegetables": ["beans", "carrot", "tomato", "onions"], "fruits": ["apples", "orange", "grapes", "mango"]})
print("the value of dict after updating is {}".format(dict3))

# reverse the values of given dict
dict_a = {"Name_1": "Abhishek", "Name_2": "Gajendra", "Name_3": "Vandana"}
print("the value of dictionary is {}".format(dict_a))

dict_a["Name_1"] = dict_a["Name_1"][::-1]
dict_a["Name_2"] = dict_a["Name_2"][::-1]
dict_a["Name_3"] = dict_a["Name_3"][::-1]
print(dict_a)

# frst_dict = dict_a["Name_1"]
# rev = frst_dict[::-1]
# print(frst_dict)

# print(rev)
# dict_a["Name_1"] = rev
# print(dict_a)

# rev_list_b = list_b[0][::-1], list_b[1][::-1], list_b[2][::-1]
# dict_b = dict(zip(list_a, rev_list_b))
# print("the value of dictionary is {}".format(dict_b))
# dict_a = {"Name_1": "Abhishek", "Name_2": "Gajendra", "Name_3": "Vandana"}
# print("the value of dictionary is {}".format(dict_a))
# val_dict = list(dict_a.values())[0][::-1], list(dict_a.values())[1][::-1], list(dict_a.values())[2][::-1]
# print(" the values in dictionary are {}".format(val_dict))
# get_keys = dict_a.keys()
# print("the keys in the dictionary are {}".format(get_keys))

values = list(dict_a.values())
lst_val = list((values[0][::1], values[1][::1], values[2][::1]))
print("the list of reversed values are {}".format(lst_val))

dict_a["Name_1"] = lst_val[0]
dict_a["Name_2"] = lst_val[1]
dict_a["Name_3"] = lst_val[2]
print("the value of dict after reversing values are {}".format(dict_a))

dict3 = {"vegetables": ["beans", "carrot"], "fruits": ["apples", "orange"]}
# dict3["vegetables"] = dict3["vegetables"].append("Onion")
# dict3["fruits"] = dict3["fruits"].append("Grapes")
# print("the value of dict after updating is {}".format(dict3))

# fst = dict3["vegetables"]
# fst_lst = list(fst).append("a")
# print(fst_lst)
value = list(dict3.values())
val_app = [value[0]+["Onion"], value[1]+["Grapes"]]
dict3["vegetables"] = val_app[0]
dict3["fruits"] = val_app[1]
print(dict3)