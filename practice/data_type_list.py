a = []
print("the type of variable a is{}".format(a))

lst = list()
print("the type of variable lst is {}".format(lst))

lst = [6, 1, 5, "10", "welcome", "hello", "$"]
print("the value of list is {}".format(lst))

type_lst = type(lst)
print("the type of variable lst is {}".format(type_lst))

#indexing the list
b = ["python", "123","!" , 16, 0]
print("the value of variable b is {}".format(b))
len_b = len(b)
print("the length of the variable b is {}".format(len_b))

zeroth_ind_b = b[0]
print("the value of zeroth index of lst is {}".format(zeroth_ind_b))
frst_ind_b = b[1]
print("the value of first index of lst is {}".format(frst_ind_b))
sec_ind_b = b[2]
print("the value of second index of lst is {}".format(sec_ind_b))
thrd_ind_b = b[3]
print("the value of thrd index of lst is {}".format(thrd_ind_b))
frth_ind_b = b[4]
print("the value of fourth index of lst is {}".format(frth_ind_b))

#slicing
p = [12, 13, "ab", "&", "xyz", 14, 15]
print("the value of variable p is {}".format(p))
p_zero_to_two_ind = p[0:3]
print("the value of slicing from zero to second index of list is {}".format(p_zero_to_two_ind))
p_three_to_six_ind = p[3:7]
print("the value of slicing from third to sixth index of list is {}".format(p_three_to_six_ind))
p_zero_to_three_ind = p[0:4]
print("the value of slicing from zero to third index of list is {}".format(p_zero_to_three_ind))

lst_zero_to_sec_ind = lst[0:3]
print("the value of slicing from zero to sec index of list is {}".format(lst_zero_to_sec_ind))
lst_three_to_six_ind = lst[3:7]
print("the value of slicing from three to six index of list is {}".format(lst_three_to_six_ind))

lst_y = [1, "python"]
print(lst_y[1][2:6])
print(lst_y[1][-6:-1])

lst_y_zero_to_four = lst_y[0:5]
print("the value of slicing from zero to four is {}".format(lst_y_zero_to_four))

lst_y_five_neg_one= lst_y[1][-5:-1]
print("the value of negative slicing is {}".format(lst_y_five_neg_one))
print(lst_y[1][0:-1])
print(lst_y[1][-5:5])
print(lst_y[1][-6:-2])
print(lst_y[1][-3:-1])

lst = ["vandana", "abhishek", "gajendra", "manasa"]
frst_rev_lst = lst[0][::-1]
print("the value of first reverse index is {}".format(frst_rev_lst))
sec_rev_lst = lst[1][::-1]
print("the value of second reverse index is {}".format(sec_rev_lst))
thrd_rev_lst = lst[2][::-1]
print("the value of first reverse index is {}".format(thrd_rev_lst))
frth_rev_lst = lst[3][::-1]
print("the value of forth reverse index is {}".format(frth_rev_lst))

print("the value of lst is {}".format(lst))
print("the value of reverse lst is {}, {}, {}, {} ".format(frst_rev_lst, sec_rev_lst, thrd_rev_lst, frth_rev_lst))

# another way
rev_lst = lst[0][::-1], lst[1][::-1], lst[2][::-1], lst[3][::-1]
print("the value of reversed list is {}".format(rev_lst))

# list concatination
lst1 = ["a", "b", "c"]
lst2 =[1,2,3]
lst_con = lst1 + lst2
print("the value of lst after concatinating is {}".format(lst_con))

em_lst = []
em_lst.append("vandana")
print("the value of list after appending list is {}".format(em_lst))

# finding min and max numbers from list
lst_a = [10, 1, 0, 12, 16, 100]
max_num = max(lst_a)
min_num = min(lst_a)
print("The minimum number in list is {}".format(min_num))
print("The maximum number in list is {}".format(max_num))

# converting tuple to list
tple = ("a", "b", 1)
tple_to_lst = list(tple)
print("the value of converted tuple is {}".format(tple_to_lst))

# count the object occured in list

lst_b = [1, "a", "1", 2, 1]
count_int_1 = lst_b.count(1)
print("The count of element or object  of int 1 is {}".format(count_int_1))
count_str_1 = lst_b.count("1")
print("The count of element or object  of str 1 is {}".format(count_str_1))

# finding index of an object
ind_obj = lst_b.index("a")
print("The index value of object a is {}".format(ind_obj))

# inserting an object with the reference of index value
lst_b.insert(3, "c")
print("the value of list after inserting 3 to list is {}".format(lst_b))

# pop elmeent from list
lst_b.pop()
print("The value of list after popping an elemnt is {}".format(lst_b))
lst_b.pop(1)
print("the value of list after popping 1st index value is {}".format(lst_b))

# remove in list
lst_b.remove("1")
print("The value of list after removing string 1 is {}".format(lst_b))

# reverse in list
lst_b.reverse()
print("The value of list after reversing is {}".format(lst_b))

# sorting in list
lst_c = [5, 4, 9, 8, 10, 20, 6]
lst_c.sort()
print("The value of list after sorting is {}".format(lst_c))

# zip in list
lsta = ["a", "b"]
lstb = [1, 2]
lst_zip =  list(zip(lsta, lstb))
print("The value after zipping 2 lists is {}".format(lst_zip))

sum_lstc = sum(lst_c)
print("The sum of list is {}".format(sum_lstc))

list = [5, 7, 2, 1, 0, 10, 8]
list.sort()
print(" the value of list in ascending order is {}".format(list))
list.reverse()
print("the value of list in descending order is {}".format(list))
