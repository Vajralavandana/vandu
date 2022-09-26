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

#adding values to existing dict
dict3.update({"vegetables": ["beans", "carrot", "tomato", "onions"], "fruits": ["apples", "orange", "grapes", "mango"]})
print("the value of dict after updating is {}".format(dict3))

dict_a ={"Name_1": "Abhishek", "Name_2": "Gajendra", "Name_3": "Vandana"}
print("the value of dictionary is {}".format(dict_a))

dict_a["Name_1"] = "kehsihhbA"
dict_a["Name_2"] = "ardnejaG"
dict_a["Name_3"] = "anadnaV"
print("the value of reversed dict is {}".format(dict_a))