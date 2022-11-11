s = "abcabcbb"
# output = 3
emp = ""
for i in s:
    if i not in emp:
        emp = emp + i
len_emp = len(emp)
print(emp, len_emp)

n = input("the string is: ")
emp1 = ""
for i in n:
    if i not in emp1:
        emp1 = emp1 + i
len1 = len(emp1)
print(emp1, len1)



"""
write a program to combine two different dictionaries.
while combining, if you find the same keys, you can add the values of these same keys. output the new dictionary
o/p {"a": 1, "b": 2, "c": 7, "e":5, "d":5}
"""
dicta = {"a": 1, "b": 2, "c": 3}
dictb = {"e": 5, "c": 4, "d": 5}
d = {}
for k, v in dicta.items():
    for i, j in dictb.items():
        if k == i:
            d[k, i] = v + j
        else:
            d[k] = v
            d[i] = j
print(d)




a = "aaabbbccaabb"
# o/p = '3a3b2c2a2b'
# c = ""
# count = 0
# for i in a:
#     if i in c:
#         c = a.count(i) + 1
#     print(c)
# d = {}
# count = 0
# for i in a:
#     count = a.count(i)
#     if i in a:
#         d[i] = count
# print(d)



str = "This is India"
# o/p = the max length string is India and length is 5
str_splt = str.split()
max_len = min(str_splt)
print(max_len)
