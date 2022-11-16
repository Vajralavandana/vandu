# to check given number is prime number or not
n = int(input("Enter the value :  "))
# n = 17
for i in range(2, n):
    if n % i == 0:
        print("n is not a prime")
        break
else:
    print(("n is a prime number"))


# To list prime numbers from range 1 to 50
prime_num = []
for j in range(1, 51):
    for i in range(2, j):
        if j % i == 0:
            break
    else:
        prime_num.append(j)
print(prime_num)


# str  = "this is India"
str1 = "welcome to python"
lst = str1.split(" ")
mx_ln = 0
mx_str = ""
for i in lst:
    if len(i) > mx_ln:
        mx_ln = len(i)
        mx_str = i
print("String {} has max length {}".format(mx_str, mx_ln))

#
# # str_a = "aaabbbccaabb"
# # str_a = "aaaccbbbaabb"
# str_a = "aaaccbbbaabbd"
# res = ""
# sub_str = ""
#
#
# for i in range(len(str_a)):
#     if i ==len(str_a)-1:
#         sub_str = sub_str + str_a[i]
#         ln = len(sub_str)
#         if ln > 0:
#             res = res + str(ln) + sub_str[0]
#     elif str_a[i] not in sub_str:
#         ln = len(sub_str)
#         if ln > 0:
#             res = res + str(ln) + sub_str[0]
#         sub_str = ""
#         sub_str = sub_str+str_a[i]
#     elif str_a[i] in sub_str:
#         sub_str = sub_str+str_a[i]
# print(res)

s = "aaabbccdde"
index = 0
str_rep = ""
while (index<= len(s)-1):
    count = 1
    char = s[index]
    j = index
    while(j <len(s)-1):
        if (s[j]==s[j+1]):
            count = count+1
            j = j+1
        else:
            break
    str_rep = str_rep+str(count)+char
    index = j+1
print(str_rep)



dict_a = {"a": 1, "b": 2, "c": 3}
dict_b = {"e": 5, "c": 4, "d": 5}
for k in dict_b:
    if k in dict_a:
        dict_b[k] = dict_b[k]+dict_a[k]
res = dict_a | dict_b
print(res)


str_a = "abccabcbb"
sub_str = ""
max_len = 0
for i in str_a:
    if i not in sub_str:
        sub_str = sub_str+i
        max_len = len(sub_str)
print(max_len)