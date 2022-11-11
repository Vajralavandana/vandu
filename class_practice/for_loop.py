str_a = "Hello"
for i in str_a:
    print(i)
l1 = [i for i in str_a]
print(l1)

lst_a = [1, 3, 5, 8]
for i in lst_a:
    print(i)

dict_a = {"a":1, "b":2}
for keys, values in dict_a.items():
    print(keys)
    print(values)

dict_b = {"vegetables":["Tomato", "Onion"], "fruits":["Apple", "Orange"]}
for k, v in dict_b.items():
    print(k)
    print(v)

# revere each element in the sting
str_b = "welcome to python"
splt_str = str_b.split(" ")
rev_lst = []
for i in splt_str:
    rev_lst.append(i[::-1])
rev_str = " ".join(rev_lst)
print("The reversed string is {}".format(rev_str))

l2 = [i[::-1] for i in str_b.split(" ")]
print(" ".join(l2))

tpl_a = (1, 4, 9)
for j in tpl_a:
    print(j)

set_a = {1, 6, 0}
initial = 0
for k in set_a:
    initial = k
    print(k)
print(initial)

# String reversing without using inbuilt function and without using slicing
str_b = "Deekshitha"
rev_str = ""
for i in str_b:
    print("The rev_str value before iteration is {}".format(rev_str))
    print("The value of i is {}".format(i))
    rev_str = i+rev_str
    print("the rev_str value after iteration is {}".format(rev_str))
print("The value of reversed string is {}".format(rev_str))

str_ab = "python programming"
# rev_ab = ""
l3 = [i[::-1] for i in str_ab][::-1]
print(l3)

"""
i/p :  str_b = "Welcome to python"
o/p :  rev_str_b = "emocleW ot nohtyp"
"""

# Range function
lst = list(range(10))
print("the list of values of range is {}".format(lst))
lst_a = list(range(1, 10))
print("The list of range of values from 1 to  10 is {}".format(lst_a))
lst_step = list(range(0, 110, 20))      # initial point, end point, step size
print("The list of values from 0 to 100 with stepsize 20 is {}".format(lst_step))

# summation
def summation(init_pnt, end_pnt):
    sum = 0
    for i in range(init_pnt, end_pnt):
        sum = sum + i
    return sum

print("the summation of values from 0 to 10 is {}".format(summation(0, 10)))
print("The summation of values from 0 to 100 is {}".format(summation(0, 100)))

a = summation(0, 10)
print(a)

# inner for loops
lst1 = [1, 2, 3, 4]
lst2 = [5, 6, 7, 8]
for i in lst1:
    for j in lst2:
        print(i, j)
l4 = [(i, j) for j in lst2 for i in lst1]
print(l4)

sum_lst = []
for i in range(len(lst1)):
    sum = lst1[i] + lst2[i]
    sum_lst.append(sum)
print("The sum of each elements of two list is {}".format(sum_lst))

l5 = [lst1[i] + lst2[i] for i in range(len(lst2)) if len(lst1) == len(lst2)]
print(l5)

def sumlist(list, list1):
    sum_lst = []
    for i in range(len(list)):
        sum = list[i] + list1[i]
        sum_lst.append(sum)
    return sum_lst
bc = sumlist([1, 7, 5, 3, 6], [2, 5, 10, 18, 0])
print(bc)

# try:
#     sum_lst = []
#     for i in range(len(lst1)):
#         sum = lst1[i] + lst2[i]
#         sum_lst.append(sum)
#     print("The sum of each elements of two two list is {}".format(sum_lst))
# except Exception as e:
#     print(e)


# lst_a = [2, 4, 6, 9]
# lst_b = [3, 4, 5, 2, 4]
# lst_c=[0, 1, 2]
# for i in lst_a:
#     for j in lst_b:
#         print(i, j)
#         for k in lst_c:
#             print(j, k)
#             print(i, k)
#             print(i, j, k)
#     print(i, j, k)
