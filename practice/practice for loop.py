str_b = "Welcome to python"
str_b_rev = " "
for i in str_b:
    str_b_rev= i + str_b_rev
    print("the reverse value is {}".format(str_b_rev))
str_b_rev1 = str_b_rev[10:17] + str_b_rev[6:10]+ str_b_rev[0:7]
print("the reverse string is {}".format(str_b_rev1))

str = "hello world"
str_rev = " "
for a in str:
    str_rev = a +str_rev
    print("the reverse value is {}".format(str_rev))
str1 = str_rev[6:11] + " " + str_rev[0:5]
print(str1)

str_b = list(str_b)
print(str_b)
list1 = str_b[::-1]
print(list1)
list1 = str_b[0:7] + str_b[8:10] + str_b[11:17]
print(list1)
list2 = str_b[7:0] + str_b[10:8] + str_b[17:11]
print(list2)
list1.reverse()
print(list1)


str_b = "welcome to python"
splt_str = str_b.split(" ")
rev_lst = []
for i in splt_str:
    rev_lst.append(i[::-1])
rev_str = " ".join(rev_lst)
print("The reversed string is {}".format(rev_str))

# print(" the value of string is{}".format(splt))
#
# len_splt = len(splt)
# print(" the length of split string is {}".format(len_splt))
# rev = splt[0][::-1] + " " + splt[1][::-1] + " " + splt[2][::-1]
# print("the reverse value is {}".format(rev))

# for k in splt:
#     rev = k + rev[::-1]
#     print(rev)




str1 = "welcome to the world of python"
# Print the value of string which is in the place of multiples of 3
mul = " "
for i in range(len(str1)):
    if str[i] * 3 == 0:
        mul = mul.append(str[i])
print(mul)



# Remove duplicates from the list
lst = [1,4,1,5,2,4]
emp_lst = []
for i in range(len(lst)):
    if i in lst:
        emp_lst.append(i)
print("the value of list after removing duplicates is {}".format(emp_lst))


lst2 = ["malayalam", "area", "dog"]
# Print the elements of list which is starting and ending with same letter
str = []
for i in lst2:
    if i.startswith(i[0]) and i.endswith(i[0]):
        str.append(i)
print("the list the elements starting and ending with same letter is {}".format(str))