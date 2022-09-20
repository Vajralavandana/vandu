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





