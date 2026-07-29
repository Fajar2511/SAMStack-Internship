import numpy as np

print(" TASK 1: Create 1D, 2D, and 3D Arrays:")
Array1 = np.array([1, 2, 3, 4, 5])
Array2 = np.array([[1, 2, 3], 
                   [4, 5, 6], 
                   [7, 8, 9]])
Array3 = np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9]], 
                   [[10, 11, 12], [13, 14, 15], [16, 17, 18]]])

print("Array1:", Array1)
print("Shape:", Array1.shape, " Size:", Array1.size, "ndim:", Array1.ndim, "\n")
print("Array2:\n", Array2)
print("Shape:", Array2.shape, " Size:", Array2.size, " ndim:", Array2.ndim, "\n")
print("Array3:\n", Array3)
print("Shape:", Array3.shape, " Size:", Array3.size, " ndim:", Array3.ndim, "\n")

print("TASK 2: Built-in Generation Functions")
zeros_matrix = np.zeros((4, 4))
print("4x4 Zeros Matrix:\n", zeros_matrix, "\n")

range_array = np.arange(10, 51, 5)
print("Array 10 to 50 step 5:\n", range_array, "\n")
linspace_array = np.linspace(0, 1, 20)
print("20 numbers between 0 and 1:\n", linspace_array, "\n")

print("TASK 3: Matrix Indexing & Slicing ")
matrix = np.arange(1, 26).reshape(5, 5)
print("Original 5x5 Matrix:\n", matrix, "\n")
print("Entire 3rd Row:", matrix[2, :])
print("Entire 4th Column:", matrix[:, 3])
print("2x2 Top-Right Sub-matrix:\n", matrix[0:2, 3:5])