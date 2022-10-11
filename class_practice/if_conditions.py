# to check even number

num = int(input("The number is : "))        # by default input function takes string
if num%2 == 0:
    print("The given number is even")
else:
    print("The given number is not even")

# find the largest number among 3

a = int(input("Tha value a is : "))
b = int(input("The valu of b is : "))
c = int(input("The value of c is: "))
if a>b and a>c:
    print("a is largest number")
elif b>a and b>c:
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
def ascending_order(lst):
    len_lst = len(lst)
    for i in range(len_lst):
        for j in range(i+1, len_lst):
            print(i)
            print(j)
            print(lst[i])
            print(lst[j])
