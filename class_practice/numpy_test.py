import numpy as np
arr = np.array([1, 2, 3, 6, 9])
print(arr)

arr_mult_dim = np.array([[1, 2, 3], [4, 5, 6]])
print(arr_mult_dim)

arr_dim = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [3, 2, 1]]])
print(arr_dim)
print(arr[1]+arr[2])
print("2nd element on 1st row", arr_mult_dim[0, 1])
print(arr_dim[0, 1, 2])
print(arr_dim[1, 1, 2])
arr_dimm = np.array([[[1, 2, 3], [4, 5, 6]], [[2, 4, 6], [3, 5, 7]], [[7, 8, 9], [3, 2, 1]]])
print(arr_dimm[1, 1, 2])
print(arr_dimm[1, 1])

print(arr_dimm[0, 1, 1])
print("last element from 2nd dim:", arr_mult_dim[1, -1])
print(arr[0:2])

print(arr_mult_dim[1, -2])
print(arr_mult_dim[0, 1:2])

import numpy as nm
ar = nm.array([8, 5, 9, 7])
print(ar)
mul_di = nm.array([[2, 4, 6, 7], [8, 3, 5, 9]])
print(mul_di)

a_m_d = nm.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [0, 1, 5]]])
print(a_m_d)
print(ar[1] + ar[2])
print(a_m_d[0, 1])
print(a_m_d[1, 0])
print(a_m_d[1, -1])
print(a_m_d[0, 0:1])
print(a_m_d[0, -1])

