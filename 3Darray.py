import numpy as np
matrix1=np.array([[1,2,3],[2,4,6],[1,3,5]])
matrix2=np.array([[0,1,2],[2,3,4],[4,5,6]])
print("Original 3D matrix : ")
print(matrix1)
print(matrix2)
print("Outer product of the two matrix : ")
result = np.outer(matrix1,matrix2)
print (result)
