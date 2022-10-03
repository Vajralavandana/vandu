str = "python"
len_str = len(str)
print(len_str)

frst_ind_str = str[0]
print(frst_ind_str)

frst_neg_ind_str = str[-1]
print(frst_neg_ind_str)

type_str = type(str)
print(type_str)

zeroth_to_three_ind = str[0:4]
print(zeroth_to_three_ind)

zero_to_ind = str[::-1]
print(zero_to_ind)

str_rev = str[::-1]
print(str_rev)

stra = "welcome to python"
splt_stra = stra.split(" ")
print(splt_stra)

join_splt = ":".join(splt_stra)
print(join_splt)

print("the value of str is {}".format(stra.find("to")))
print("the value of str is {}".format(stra.index("o")))
print("the value of str is {}".format(stra.count("p")))
print("the value of str is {}".format(stra.startswith("to")))
print("the value of str is {}".format(stra.startswith("w")))
print("the value of str is {}".format(stra.endswith("n")))
print("the value of str is {}".format(stra.capitalize()))
is_alpha_str = stra.isalpha()
print("the value of str is {}".format(is_alpha_str))
print("the value of str is {}".format(stra.lower()))
is_Upp = stra.upper()
print("the value of str is {}".format(is_Upp))
print("the value of str is {}".format(stra.lower()))
print("the value of str is {}".format(stra.upper()))
print("the value of str is {}".format(stra.swapcase()))



# list
lst = [1, 2, 3, "a", "b"]
len_lst = len(lst)
print(len_lst)

type_lst = type(lst)
print(type_lst)

lst.reverse()
print(lst)

zero_to_ind_lst = lst[0]
print(zero_to_ind_lst)

neg_ind_lst = lst[-1]
print(neg_ind_lst)

slicing_lst = lst[0:3]
print(slicing_lst)

rev_lst = lst[::-1]
print(rev_lst)

a = [1, 2, 3, 7, 2]
b = [21, 3, 4, 89]
min_nm = min(a)
print(min_nm)
max_nm = max(a)
print(max_nm)

print("the value of lst is {}".format(a.count(2)))
a.pop()
print(a)

a.remove(2)
print(a)

lsta = ["a", "b"]
lstb = [1, 2]
zip_lst = list(zip(lsta, lstb))
print(zip_lst)

sum_a = sum(a)
print(sum_a)

a.sort()
print(a)

# tuple
tpl = ("a", 1, 3, "python")
t = (1, 2, 5, 6, 90)
min_t = min(t)
max_t = max(t)
print(min_t)
print(max_t)

#dict
d ={"a":1, "b":2}
d.update({"d":3, "c":4})
print(d)

get_keys = d.keys()
print(get_keys)

get_values = d.values()
print(get_values)

get_ele = d.get("a")
print(get_ele)

d.pop("d")
print(d)

d.popitem()
print(d)

clear_d =d.clear()
print(clear_d)

s = {1, 2, 4, 7}
s.add(8)
print(s)

upd_set ={10, 11}
s.update(upd_set)
print(s)

s.remove(1)
print(s)

s.discard(2)
print(s)

s.pop()
print(s)
