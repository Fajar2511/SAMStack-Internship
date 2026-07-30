import numpy as np

print("TASK 1: Reshaping & Array Manipulation")
arr_1d = np.arange(1, 25)
print("1D Array:", arr_1d)

arr_3d = arr_1d.reshape(2, 3, 4)
print("3D Array shape (2,3,4):\n", arr_3d)
flat_copy = arr_3d.flatten() 
ravel_view = arr_3d.ravel() 
print("Flatten - Copy:", flat_copy)
print("Ravel - View:", ravel_view)
arr_3d[0, 0, 0] = 99
print("\nAfter changing arr_3d[0,0,0] to 99:")
print("Flatten Copy:", flat_copy) 
print("Ravel View:", ravel_view)  

print("TASK 2: Vectorized Math & Broadcasting ")

mat1 = np.random.randint(1, 11, (3, 3))
mat2 = np.random.randint(1, 11, (3, 3))
print("Matrix 1:\n", mat1)
print("Matrix 2:\n", mat2)
elem_mul = mat1 * mat2
print("Element-wise Multiplication *:\n", elem_mul)
matrix_mul = mat1 @ mat2
print("Matrix Multiplication @:\n", matrix_mul)

add_array = np.array([10, 20, 30])
broadcasted = mat1 + add_array
print("Broadcasting [10,20,30] + Matrix1:\n", broadcasted)

print("\n TASK 3: Boolean Masking & Conditional Filtering ")

arr_20 = np.random.randint(10, 101, 20)
print("Original 20 numbers:", arr_20)

greater_50 = arr_20[arr_20 > 50]
print("Numbers > 50:", greater_50)

arr_20[arr_20 % 2 == 1] = -1
print("After replacing odds with -1:", arr_20)