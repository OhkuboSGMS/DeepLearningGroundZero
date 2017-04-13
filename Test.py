import numpy as np
import matplotlib.pyplot as plt
from matplotlib.image import imread
x =np.array([1.0,2.0,3.0])
y =np.array([2.0,4.0,6.0])
print(x)
print(type(x))
#element-wise 要素ごと

print (x+y)
print(x*y)

z =np.array([[1,2] ,[3,4]])
print(z)

print(z[0])
print(z[0][0])

x =np.arange(0,6,0.1)
y =np.sin(x)

img =imread("subpiece.png")
plt.imshow(img)
# plt.show()
#plt.plot(x,y)

A  =np.array([1,2,3,4])
print(A)
print(np.ndim(A))
print(A.shape)
print(A.shape[0])

B =np.array([[1,2],[3,4],[4,5]])
print(B)
print(np.ndim(B))
print(B.shape)