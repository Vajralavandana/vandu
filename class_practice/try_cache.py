




lst1 = [1, 2, 3, 4, 9]
lst2 = [5, 6, 7, 8]
try:
    sum_lst = []
    for i in range(len(lst1)):
        sum = lst1[i] + lst2[i]
        sum_lst.append(sum)
    print("The sum of each elements of two two list is {}".format(sum_lst))
except Exception as e:
    print(e)


n= int(input("Enter the value : "))
try:
    if n%2 ==0:
        print("The given value is even")
    else:
        print("Tthe given value is odd")
except:
    print("Eexception occured")
else:
    print("went good without any exception")

lst1 = [1, 2, 3, 4, 9]
lst2 = [5, 6, 7, 8]
try:
    sum_lst = []
    for i in range(len(lst1)):
        sum = lst1[i] + lst2[i]
        sum_lst.append(sum)
    print("The sum of each elements of two two list is {}".format(sum_lst))
except Exception as e:
    print(e)
finally:
    lst = lst1+lst2
    print(lst)
