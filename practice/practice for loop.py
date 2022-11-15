# str_b = "Welcome to python"
# str_b_rev = " "
# for i in str_b:
#     str_b_rev= i + str_b_rev
#     print("the reverse value is {}".format(str_b_rev))
# str_b_rev1 = str_b_rev[10:17] + str_b_rev[6:10]+ str_b_rev[0:7]
# print("the reverse string is {}".format(str_b_rev1))
#
# st = "hello world"
# str_rev = " "
# for a in st:
#     str_rev = a +str_rev
#     print("the reverse value is {}".format(str_rev))
# str1 = str_rev[6:11] + " " + str_rev[0:5]
# print(str1)

# str_b = list(str_b)
# print(str_b)
# list1 = str_b[::-1]
# print(list1)
# list1 = str_b[0:7] + str_b[8:10] + str_b[11:17]
# print(list1)
# list2 = str_b[7:0] + str_b[10:8] + str_b[17:11]
# print(list2)
# list1.reverse()
# print(list1)

# reverse each word in string
str_b = "welcome to python"
splt_str = str_b.split(" ")
rev_lst = []
for i in splt_str:
    rev_lst.append(i[::-1])
rev_str = " ".join(rev_lst)
print("The reversed string is {}".format(rev_str))

str_lm = [i[::-1] for i in str_b.split(" ")]
print(str_lm)

def rev(str):
    splt_str = str.split(" ")
    rev_lst = []
    for i in splt_str:
        rev_lst.append(i[::-1])
    rev_str = " ".join(rev_lst)
    return rev_str
a = rev("hello welcome to world")
print(a)

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
for k in range(3, 30, 3):
    print(str1[k])

l6 = [str1[i] for i in range(3, 30, 3)]
print(l6)

# def multiple_of_three(str):
#     str_v = ""
#     for i in range(3, 30, 3):
#         str_v = str_v + str[i]
#     return str_v

# str_ab = multiple_of_three("welcome to home")
# print("multiples of 3 is {}".format(str_ab))

# Remove duplicates from the list
lst = [25, 20, 9, 25, 20, 10]
emp_lst = []
for i in lst:
    if i not in emp_lst:
        emp_lst.append(i)
print("the value of list after removing duplicates is {}".format(emp_lst))

# l7 = [i for i in lst if i not in emp_lst]
# print(l7)

def rem_dup(list):
    em_lst = []
    for i in list:
        if i not in em_lst:
            em_lst.append(i)
    return em_lst
c = rem_dup([3,56,32,1,4,3,1,32,67, 6, 3, 6, 678,24, 67, 34, 32,0, 89, 34])
print(c)

lst2 = ["malayalam", "area", "dog"]
# Print the elements of list which is starting and ending with same letter
emplst = []
for i in lst2:
    if i.startswith(i[0]) and i.endswith(i[0]):
        emplst.append(i)
print("the list the elements starting and ending with same letter is {}".format(emplst))
#otherway
for i in lst2:
    if i[0] == i[-1]:
        print(i)

l8 = [i for i in lst2 if i[0] == i[-1]]
print(l8)

def start_end(list):
    for i in list:
        if i[0] == i[-1]:
            return i
d = start_end(["level", "vandana", "malayalam", "sky", "ana", "bcbb"])
print(d)

# difference between num and reverse of same number
num = int(input("The number is: "))
str_num = str(num)
rev = str_num[::-1]
int_num = int(rev)
print("the reverse number is {}".format(rev))
diff = num - int_num
print("the difference between the numbers is {}".format(diff))

def diff(num):
    str_numb = str(num)
    reve = str_numb[::-1]
    int_numb = int(reve)
    print(reve)
    diffe = num - int_numb
    return diffe
e = diff(45)
print(e)

list = ["malayalam", "area", "aba", "xyz", "see", "1221", "god"]
#count of elements starts and ends with same letter
count = 0
for i in list:
    if i[0] == i[-1]:
        count = count + 1
print("the count of elements starting and ending with same letter is {}".format(count))

l9 = [i for i in list if i[0] == i[-1]]
print(len(l9))

def cont(list):
    count = 0
    for i in list:
        if i[0] == i[-1]:
            count = count + 1
    return count
f = cont(["121", "1234", "abdfa", "rtwdr", "hjkfl"])
print(f)

lst1 = [4, 25, -2, 0, -9, 10, 3, 1]
# print 2 lists of positive list and negative list without duplicates
pos = []
neg = []
for i in lst1:
    if i >= 0 and i not in pos:
        pos.append(i)
    if i < 0 and i not in neg:
        neg.append(i)
print(pos)
print(neg)

l10 = [i for i in lst1 if i >= 0]
l100 = [i for i in lst1 if i < 0]
print(l10, l100)

def pos_neg_list(list):
    pos = []
    neg = []
    for i in list:
        if i >= 0 and i not in pos:
            pos.append(i)
        if i < 0 and i not in neg:
            neg.append(i)
    return pos, neg
ab = pos_neg_list([1, -4, 67, 87, -3, -8, 456, -9])
print(ab)

# remove duplicates from string
str_a = "hgdkogfkkazmv591469sgh123agh"
s = []
for j in str_a:
    if j not in s:
        s.append(j)
st = "".join(s)
print(st)
# another way
str_a = "hgdkogfkkazmv591469sgh123agh"
s = []
# for i in str_a:
#     if i not in s:
#         s = s + i
# print("the string after removing duplicates is {}".format(s))



def rem_str(str):
    x = ""
    for i in str:
        if i not in x:
            x = x + i
    return x
g = rem_str("hgdkogfkkazmv591469sgh123aghghgdtrdykittrewersrdtryrdyytrdrtetriiiiewwa")
print(g)

# Write a program to find N largest number from list
lst_a = [5, 56, 17, 87, 34, 2, 76]
# lst_a.sort()
# desc_lst = []
# for i in lst_a:
#     desc_lst = [i] + desc_lst
# print(desc_lst)
# n = int(input("Enter the number: "))
# m = desc_lst[0:n]
# print(m)

# another way
# lst_c = [5, 56, 17, 87, 34, 2, 76]
# lst_c.sort()
# lst_c.reverse()
# print(lst_c)
# N = int(input("N ="))
# lar_lst = []
# for i in range(N):
#     lar_lst.append(lst_c[i])
# print(lar_lst)

# another way
lst_b = [5, 56, 17, 87, 34, 2, 76]
lst_b.sort()
lst_b.reverse()
print(lst_b)
N = int(input("N ="))
for i in range(N):
    print(lst_b[i])


def lar_num(list, N):
    list.sort()
    list.reverse()
    large_lst = []
    for i in range(N):
        large_lst.append(lst_b[i])
    return large_lst

a = lar_num([5, 56, 17, 87, 34, 2, 76], 2)
print(a)

str1 = "abcdfcdaecbajadej"
# output: dict_a ={"a":4,"b":2,"c":3,"d":3,"j":2,"e":2, "f":1}
str1_dict = {}
for i in str1:
    cnt = str1.count(i)
    str1_dict[i] = cnt
print(str1_dict)

l12 = {i: str1.count(i) for i in str1}
print(l12)

def str_dictionary(str):
    str12_dict = {}
    for i in str1:
        cnt1 = str.count(i)
        str12_dict[i] = cnt1
    return str12_dict
b = str_dictionary("abcdfcdaecbajadejagf")
print(b)

# remove vowels in str
str12 = "hai how are you"
lstx = ["a", "e", "i", "o", "u"]
j = []
for i in str12:
    if i not in lstx:
        j.append(i)
jn = "".join(j)
print(jn)

l13 = [i for i in str12 if i not in lstx]
print(" ".join(l13))

def vow_rem(str):
    j = []
    for i in str:
        if i not in lstx:
            j.append(i)
    jn = "".join(j)
    return jn
v = vow_rem("welcome to sweet home")
print(v)

# vowels count in dict
d = {}
count = 0
for i in str12:
    count = str12.count(i)
    if i in lstx:
        d[i] = count
print(d)

# str12 = "hai welcome you all"
# lstx = ["a", "e", "i", "o", "u"]
l14 = {i: str12.count(i) for i in str12 if i in lstx}
print(l14)

lt = ["a", "e", "i", "o", "u"]
def vo_coun(str):
    c = {}
    count = 0
    for i in str:
        count = str.count(i)
        if i in lt:
            c[i] = count
    return c
g = vo_coun("welcome to python programming and world")
print(g)
h = vo_coun("hello world")
print(h)

# print prime numbers
n = int(input("number is : "))
for i in range(1, n):
    if n % i == 0:
        print(i)







