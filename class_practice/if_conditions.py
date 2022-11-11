# to check even number
num = int(input("The number is : "))        # by default input function takes string
if num % 2 == 0:
    print("The given number is even")
else:
    print("The given number is not even")

# find the largest number among 3
a = int(input("Tha value a is : "))
b = int(input("The value of b is : "))
c = int(input("The value of c is: "))
if a > b and a > c:
    print("a is largest number")
elif b > a and b > c:
    print("b is largest number")
else:
    print("c is largest number")

# if a>b:
#     if a>c:
#         print("a is largest ")
#
# elif b>a:
#     if b>c:
#         print("b is largest")
# else:
#     print("c is largest")

# ascending order of list without using inbuilt
lst = [3, 0, 5, 4]
len_lst = len(lst)
for i in range(len_lst):
    for j in range(i + 1, len_lst):
        if lst[i] > lst[j]:
            lst[i], lst[j] = lst[j], lst[i]
print(lst)

def asc_order(list):
    len_list = len(list)
    for i in range(len_list):
        for j in range(i + 1, len_list):
            if list[i] > list[j]:
                list[i], list[j] = list[j], list[i]
    return list

a = asc_order([4,8, 2, 1, 99, 3])
print(a)

# descending order of list
for i in range(len_lst):
    for j in range(i + 1, len_lst):
        if lst[i] < lst[j]:
            lst[i], lst[j] = lst[j], lst[i]
print(lst)

# find the list of even numbers and list of odd number from given list
lst_a = [2, 6, 9, 13, 22, 10, 33, 21, 4, 8]
even_lst = []
odd_lst = []
for num in lst_a:
    if num % 2 == 0:
        even_lst.append(num)
    else:
        odd_lst.append(num)
print("even list is {}".format(even_lst))
print("odd list is {}".format(odd_lst))

lcm1 = [i for i in lst_a if i % 2 == 0]
lcm2 = [i for i in lst_a if i % 2 == 1]
print(lcm1, lcm2)


def even_odd_list(list):
    even_lst = []
    odd_lst = []
    for i in list:
        if i % 2 == 0:
            even_lst.append(i)
        else:
            odd_lst.append(i)
    return even_lst, odd_lst
ab = even_odd_list([2, 5, 7, 8, 756, 0, 20, 88, 99, 55, 33])
print(ab)