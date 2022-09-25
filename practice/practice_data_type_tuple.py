#tuple
a = (5, "abc","1234","welcome",10)
print("the value of the variable a is {}".format(a))

b = (1, 2, 3, "pqr", "vandana", "%")
print("the value of the variable b is {}".format(b))

#indexing
len_a = len(a)
print("the length of the variable a is {}".format(len_a))
zeroth_ind_a = a[0]
print("the value of zeroth index of tuple is {}".format(zeroth_ind_a))
frst_ind_a = a[1]
print("the value of frst index of tuple is {}".format(frst_ind_a))
sec_ind_a = a[2]
print("the value of second index of tuple is {}".format(sec_ind_a))
thrd_ind_a = a[3]
print("the value of third index of tuple is {}".format(thrd_ind_a))
frth_ind_a = a[4]
print("the value of frth index of tuple is {}".format(frth_ind_a))

len_b = len(b)
print("the length of the variable b is {}".format(len_b))
zeroth_ind_b = b[0]
print("the value of zeroth index of tuple is {}".format(zeroth_ind_b))
frst_ind_b = b[1]
print("the value of frst index of tuple is {}".format(frst_ind_b))
sec_ind_b = b[2]
print("the value of second index of tuple is {}".format(sec_ind_b))
thrd_ind_b = b[3]
print("the value of third index of tuple is {}".format(thrd_ind_b))
frth_ind_b = b[4]
print("the value of frth index of tuple is {}".format(frth_ind_b))
fvth_ind_b = b[5]
print("the value of fvth index of tuple is {}".format(fvth_ind_b))

#slicing
c = (1, 2, 3, "@", "pqr", "welcome", 100)
len_c = len(c)
print("the length of the c is {}".format(len_c))
c_zero_to_four_ind = c[0:5]
print("the value of slicing from zero to forth index of c is {}".format(c_zero_to_four_ind))
c_fourth_to_six_ind = c[4:7]
print ("the value of slicing from fourth to six index of c is {}".format(c_fourth_to_six_ind))

tpl = (0, 1, 2, 3, 4, 4, 5, 6)
len_tpl = len(tpl)
print("The length of tuple is {}".format(len_tpl))

tple = (6, 2, 0, 2, 1, 10, 12, 0, -1)
min_num = min(tple)
max_num = max(tple)
print("The maximum value in tuple is {}".format(max_num))
print("The minimum value in tuple is {}".format(min_num))

tp1 = (1, 2, 3, 4, 5,)
tp2 = (6, 7, 8, 9, 10)
con_tp = tp1 + tp2
print("the value of tuple after concatination is {}".format(con_tp))