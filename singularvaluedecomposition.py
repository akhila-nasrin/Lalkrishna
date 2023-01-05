from numpy import array
from numpy import diag
from numpy import dot
from scipy.linalg import svd
A=array([[1,2,1],[4,5,4],[7,8,6]])
print(A)
U,s,VT=svd(A)
print(U)
print(s)
print(VT)
Sigma=diag(s)
B=U.dot(Sigma.dot(VT))
print(B)
