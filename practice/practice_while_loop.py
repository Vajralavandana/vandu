s = "abcabcbb"
# output = 3

"""
write a program to combine two different dictionaries.
while combining, if you find the same keys, you can add the values of these same keys. output the new dictionary
o/p {"a": 1, "b": 2, "c": 7, "e":5, "d":5}
"""





a = "aaabbbccaabb"
# o/p = '3a3b2c2a2b'
c = ""
for i in a:
    if i in c:
        c = c + i
    print(i)



str = "This is India"
# o/p = the max length string is India and length is 5
str_splt = str.split()
max_len = min(str_splt)
print("the max length string is {} and length is {}".format(max_len, len(max_len)))

